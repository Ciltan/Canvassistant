import os
import json
import logging
import requests
import asyncio
import base64
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# Third-party libraries
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from supabase import create_client, Client
from openai import OpenAI

# Load environment variables (.env locally, Secrets in GitHub)
load_dotenv()

# Configuration (Read directly from environment variables)
CANVAS_BASE_URL = os.getenv("CANVAS_BASE_URL")
CANVAS_TOKEN = os.getenv("CANVAS_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GDRIVE_FOLDER_ID = os.getenv("GDRIVE_FOLDER_ID")
GDRIVE_CREDS_JSON = os.getenv("GDRIVE_CREDS_JSON")  # Entire JSON string
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Local directories
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
TEMP_CREDS_FILE = Path(__file__).parent / "temp_gdrive_creds.json"

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def telegram_notify(message):
    """Send a message to the user via Telegram."""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        logger.warning("Telegram credentials missing. Could not send notification.")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"})
    except Exception as e:
        logger.error(f"Failed to send Telegram message: {e}")

class CanvasPipeline:
    def __init__(self):
        self.headers = {"Authorization": f"Bearer {CANVAS_TOKEN}"}
        
        # Initialize Supabase
        if not SUPABASE_URL or not SUPABASE_KEY:
            raise ValueError("Supabase configuration missing.")
        self.supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Initialize Google Drive (Handle JSON string from GitHub Secret)
        self.gdrive_service = self.init_gdrive()
        
        # Initialize OpenAI
        self.openai_client = OpenAI(api_key=OPENAI_API_KEY)

    def init_gdrive(self):
        if not GDRIVE_CREDS_JSON:
            raise ValueError("GDRIVE_CREDS_JSON secret is missing.")
        
        # Write JSON string to temp file for the Google client library to read
        with open(TEMP_CREDS_FILE, 'w') as f:
            f.write(GDRIVE_CREDS_JSON)
        
        try:
            creds = service_account.Credentials.from_service_account_file(
                str(TEMP_CREDS_FILE), scopes=['https://www.googleapis.com/auth/drive.file']
            )
            return build('drive', 'v3', credentials=creds)
        finally:
            # Delete temp file immediately for security
            if TEMP_CREDS_FILE.exists():
                TEMP_CREDS_FILE.unlink()

    def is_file_seen(self, file_id):
        """Check Supabase for existing file_id."""
        response = self.supabase.table("seen_files").select("file_id").eq("file_id", str(file_id)).execute()
        return len(response.data) > 0

    def mark_file_seen(self, file_id):
        """Insert seen file_id into Supabase."""
        self.supabase.table("seen_files").insert({"file_id": str(file_id)}).execute()

    def get_active_courses(self):
        url = f"{CANVAS_BASE_URL}/api/v1/courses"
        params = {"enrollment_state": "active", "per_page": 100}
        courses = []
        while url:
            resp = requests.get(url, headers=self.headers, params=params)
            resp.raise_for_status()
            courses.extend(resp.json())
            url = None
            link = resp.headers.get("Link", "")
            if 'rel="next"' in link:
                for part in link.split(","):
                    if 'rel="next"' in part:
                        url = part[part.index("<")+1 : part.index(">")]
                        params = {}
        return courses

    def get_course_files(self, course_id):
        url = f"{CANVAS_BASE_URL}/api/v1/courses/{course_id}/files"
        params = {"per_page": 100}
        files = []
        while url:
            resp = requests.get(url, headers=self.headers, params=params)
            resp.raise_for_status()
            files.extend(resp.json())
            url = None
            link = resp.headers.get("Link", "")
            if 'rel="next"' in link:
                for part in link.split(","):
                    if 'rel="next"' in part:
                        url = part[part.index("<")+1 : part.index(">")]
                        params = {}
        return files

    def get_or_create_gdrive_folder(self, folder_name, parent_id):
        query = f"name = '{folder_name}' and '{parent_id}' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
        results = self.gdrive_service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
        files = results.get('files', [])
        if files:
            return files[0]['id']
        else:
            file_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder',
                'parents': [parent_id]
            }
            folder = self.gdrive_service.files().create(body=file_metadata, fields='id').execute()
            return folder.get('id')

    def upload_to_gdrive(self, file_path, folder_id):
        file_metadata = {
            'name': file_path.name,
            'parents': [folder_id]
        }
        media = MediaFileUpload(str(file_path), resumable=True)
        file = self.gdrive_service.files().create(body=file_metadata, media_body=media, fields='id, webViewLink').execute()
        return file.get('webViewLink')

    def summarize_pdf(self, file_path):
        """Encodes PDF as base64 and uses GPT-4o for summarization."""
        try:
            with open(file_path, "rb") as pdf_file:
                pdf_base64 = base64.b64encode(pdf_file.read()).decode("utf-8")

            response = self.openai_client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Please provide a concise but comprehensive summary of this lecture material. Focus on key definitions, core concepts, and potential exam topics."},
                            {"type": "input_file", "input_file": {"data": pdf_base64, "format": "pdf"}}
                        ]
                    }
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Summarization failed for {file_path.name}: {e}")
            return f"Summarization failed: {e}"

    def process(self):
        try:
            logger.info("Starting Daily Canvas Pipeline (GitHub Actions Edition)...")
            courses = self.get_active_courses()
            logger.info(f"Found {len(courses)} active courses.")

            for course in courses:
                course_id = course.get("id")
                course_name = course.get("name", f"Course_{course_id}").replace("/", "-")
                logger.info(f"Processing course: {course_name}")

                files = self.get_course_files(course_id)
                pdf_files = [f for f in files if f.get("filename", "").lower().endswith(".pdf")]
                
                if not pdf_files:
                    continue

                # Ensure course folder in GDrive
                course_folder_id = self.get_or_create_gdrive_folder(course_name, GDRIVE_FOLDER_ID)

                for file_info in pdf_files:
                    file_id = file_info.get("id")
                    filename = file_info.get("filename")

                    if self.is_file_seen(file_id):
                        continue

                    logger.info(f"New file found: {filename}")
                    
                    # 1. Download locally
                    download_url = file_info.get("url")
                    if not download_url:
                        continue
                    
                    local_path = DATA_DIR / filename
                    DATA_DIR.mkdir(exist_ok=True)
                    
                    with requests.get(download_url, headers=self.headers, stream=True) as r:
                        r.raise_for_status()
                        with open(local_path, 'wb') as f:
                            for chunk in r.iter_content(chunk_size=8192):
                                f.write(chunk)

                    # 2. Upload to GDrive
                    gdrive_link = self.upload_to_gdrive(local_path, course_folder_id)
                    logger.info(f"Uploaded to GDrive: {gdrive_link}")

                    # 3. Summarize using OpenAI GPT-4o (Base64)
                    summary = self.summarize_pdf(local_path)
                    
                    # 4. Notify Telegram
                    msg = f"📚 *New Course Material*\n\n*Course:* {course_name}\n*File:* {filename}\n\n*Summary:*\n{summary}\n\n🔗 [View on GDrive]({gdrive_link})"
                    telegram_notify(msg)

                    # 5. Clean up local file
                    local_path.unlink()
                    
                    # 6. Mark as seen in Supabase
                    self.mark_file_seen(file_id)

            logger.info("Pipeline run complete.")

        except Exception as e:
            logger.exception("Pipeline execution failed.")
            telegram_notify(f"❌ *Canvas Pipeline Error*\n\n```python\n{str(e)}\n```")

if __name__ == "__main__":
    pipeline = CanvasPipeline()
    pipeline.process()
