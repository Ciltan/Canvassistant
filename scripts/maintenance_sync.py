import os
import json
import logging
import requests
import asyncio
import base64
from pathlib import Path
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

# Third-party libraries
import pdfplumber
from supabase import create_client, Client
from openai import OpenAI

# VERSION tracking to verify deployment in logs
VERSION = "4.0"

# Load environment variables (.env locally, Secrets in GitHub)
load_dotenv(Path(__file__).parent.parent / ".env")

# Configuration (Read directly from environment variables)
CANVAS_BASE_URL = os.getenv("CANVAS_BASE_URL")
CANVAS_TOKEN = os.getenv("CANVAS_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Local directories
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def telegram_send_pdf(file_path, course_name):
    """Send a PDF document with a short caption to the user via Telegram."""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        logger.warning("Telegram credentials missing. Could not send notification.")
        return
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument"
    try:
        with open(file_path, 'rb') as doc:
            files = {'document': doc}
            data = {
                'chat_id': TELEGRAM_CHAT_ID,
                'caption': f"📚 *New Course Material*\nCourse: {course_name}\nFile: {file_path.name}",
                'parse_mode': 'Markdown'
            }
            response = requests.post(url, data=data, files=files)
            if response.status_code != 200:
                logger.error(f"Telegram sendDocument failed: {response.text}")
            response.raise_for_status()
            logger.info(f"Successfully sent {file_path.name} to Telegram.")
    except Exception as e:
        logger.error(f"Failed to send Telegram document: {e}")

def telegram_send_message(message):
    """Send a text message to Telegram (up to 4096 chars)."""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        # Truncate if somehow exceeds 4096
        safe_msg = message[:4090]
        response = requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": safe_msg, "parse_mode": "MarkdownV2"})
        if response.status_code != 200:
            logger.error(f"Telegram sendMessage failed: {response.text}")
        response.raise_for_status()
    except Exception as e:
        logger.error(f"Failed to send Telegram message: {e}")

def telegram_send_plain(message):
    """Send a plain text message to Telegram (no Markdown parsing)."""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        response = requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message[:4090]})
        if response.status_code != 200:
            logger.error(f"Telegram sendMessage failed: {response.text}")
    except Exception as e:
        logger.error(f"Failed to send Telegram message: {e}")

def telegram_notify_error(message):
    """Send a plain text error notification to Telegram."""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message[:4090]})
    except Exception as e:
        logger.error(f"Failed to send Telegram error notification: {e}")

class CanvasPipeline:
    def __init__(self):
        self.headers = {"Authorization": f"Bearer {CANVAS_TOKEN}"}
        
        # Initialize Supabase
        if not SUPABASE_URL or not SUPABASE_KEY:
            raise ValueError("Supabase configuration missing.")
        self.supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        
        # Initialize OpenAI
        self.openai_client = OpenAI(api_key=OPENAI_API_KEY)

    def is_item_seen(self, item_id):
        """Check Supabase for existing file_id in seen_files table."""
        response = self.supabase.table("seen_files").select("file_id").eq("file_id", str(item_id)).execute()
        return len(response.data) > 0

    def mark_item_seen(self, item_id):
        """Insert seen file_id into seen_files table."""
        self.supabase.table("seen_files").insert({"file_id": str(item_id)}).execute()

    def get_active_courses(self):
        url = f"{CANVAS_BASE_URL}/api/v1/courses"
        params = {"enrollment_state": "active", "per_page": 100}
        courses = []
        while url:
            try:
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
            except Exception as e:
                logger.error(f"[V{VERSION}] Error fetching courses: {e}")
                break
        return courses

    def get_course_files(self, course_id):
        """Fetches files for a course, filtered by creation date (last 48h)."""
        url = f"{CANVAS_BASE_URL}/api/v1/courses/{course_id}/files"
        params = {"per_page": 100, "sort": "created_at", "order": "desc"}
        threshold_date = datetime.now(timezone.utc) - timedelta(hours=48)
        files = []
        try:
            while url:
                resp = requests.get(url, headers=self.headers, params=params)
                if resp.status_code == 403: return []
                resp.raise_for_status()
                batch = resp.json()
                stop_paging = False
                for file_info in batch:
                    created_at_str = file_info.get("created_at")
                    if created_at_str:
                        created_at = datetime.fromisoformat(created_at_str.replace("Z", "+00:00"))
                        if created_at < threshold_date:
                            stop_paging = True
                            break
                    files.append(file_info)
                if stop_paging: break
                url = None
                link = resp.headers.get("Link", "")
                if 'rel="next"' in link:
                    for part in link.split(","):
                        if 'rel="next"' in part:
                            url = part[part.index("<")+1 : part.index(">")]
                            params = {}
            return files
        except Exception as e:
            logger.error(f"[V{VERSION}] Error fetching files for course {course_id}: {e}")
            return []

    def get_announcements(self, course_id):
        """Fetches recent announcements for a course."""
        url = f"{CANVAS_BASE_URL}/api/v1/announcements"
        params = {
            "context_codes[]": f"course_{course_id}",
            "start_date": (datetime.now(timezone.utc) - timedelta(days=2)).isoformat(),
            "active_only": True
        }
        try:
            resp = requests.get(url, headers=self.headers, params=params)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            logger.error(f"[V{VERSION}] Error fetching announcements for {course_id}: {e}")
            return []

    def get_upcoming_assignments(self, days=7):
        """Fetches all upcoming assignments across all courses."""
        upcoming = []
        courses = self.get_active_courses()
        for course in courses:
            course_id = course.get("id")
            course_name = course.get("name", "Unknown").replace("/", "-")
            url = f"{CANVAS_BASE_URL}/api/v1/courses/{course_id}/assignments"
            params = {"bucket": "upcoming", "per_page": 50}
            try:
                resp = requests.get(url, headers=self.headers, params=params)
                resp.raise_for_status()
                for asgn in resp.json():
                    asgn['course_name'] = course_name
                    upcoming.append(asgn)
            except:
                continue
        return upcoming

    def get_assignments(self, course_id):
        """Fetches all assignments for a single course."""
        url = f"{CANVAS_BASE_URL}/api/v1/courses/{course_id}/assignments"
        params = {"per_page": 50, "order_by": "due_at"}
        try:
            resp = requests.get(url, headers=self.headers, params=params)
            resp.raise_for_status()
            return resp.json()
        except:
            return []

    def send_daily_digest(self):
        """Sends a summary of assignments due in the next 7 days."""
        logger.info(f"[V{VERSION}] Preparing Daily Digest...")
        upcoming = self.get_upcoming_assignments()
        if not upcoming:
            telegram_send_plain("✅ No assignments due in the next 7 days. Enjoy your week!")
            return

        msg = "📅 *Daily To-Do List (Next 7 Days)*\n\n"
        # Sort by due date
        upcoming.sort(key=lambda x: x.get('due_at') or '9999-12-31')
        
        for asgn in upcoming:
            name = self.escape_md(asgn.get("name", ""))
            course = self.escape_md(asgn.get("course_name", ""))
            due_str = asgn.get("due_at")
            if due_str:
                due = datetime.fromisoformat(due_str.replace("Z", "+00:00")).strftime("%d %b, %H:%M")
            else:
                due = "No due date"
            msg += f"• *{name}*\n  _{course}_ | Due: {due}\n\n"
        
        telegram_send_message(msg)

    def extract_text(self, file_path):
        """Extract all text from a PDF. Returns empty string if unreadable."""
        logger.info(f"[V{VERSION}] Extracting text from {file_path.name}...")
        try:
            with pdfplumber.open(file_path) as pdf:
                return '\n'.join(page.extract_text() for page in pdf.pages if page.extract_text())
        except Exception as e:
            logger.error(f"[V{VERSION}] Text extraction failed for {file_path.name}: {e}")
            return ""

    def summarize_pdf(self, all_text):
        """Summarizes PDF text using a Map-Reduce approach."""
        try:
            if not all_text.strip():
                return "Could not extract text from PDF (it might be scanned or empty)."

            chunk_size = 12000
            overlap = 1000
            chunks = []
            start = 0
            while start < len(all_text):
                chunks.append(all_text[start : start + chunk_size])
                start += (chunk_size - overlap)

            chunk_summaries = []
            for chunk in chunks:
                response = self.openai_client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "Summarize this lecture material chunk. Focus on core concepts."},
                        {"role": "user", "content": chunk}
                    ]
                )
                chunk_summaries.append(response.choices[0].message.content)

            final_response = self.openai_client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Combine these lecture summaries into 5-8 bullet points. Highlight exam topics."},
                    {"role": "user", "content": "\n\n".join(chunk_summaries)}
                ]
            )
            return final_response.choices[0].message.content
        except Exception as e:
            return f"Summarization failed: {e}"

    def generate_obsidian_note(self, all_text, filename, course_name):
        """Generate a structured Obsidian Markdown note from PDF text and save it.

        Notes are module-scoped: wikilinks only reference concepts within the same module.
        Each note links back to MOD_INDEX.md for navigation.
        """
        try:
            today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            stem = Path(filename).stem
            module_code = course_name.split(" ")[0].upper()

            # Read existing notes in this module to enable smart wikilinks
            note_dir = BASE_DIR / "vault" / module_code
            note_dir.mkdir(parents=True, exist_ok=True)
            existing_notes = [f.stem for f in note_dir.glob("*.md") if f.stem != "MOD_INDEX"]

            existing_notes_str = ", ".join(existing_notes[:50]) if existing_notes else "(none yet)"

            prompt = f"""You are a study assistant creating Obsidian vault notes for the module {module_code}.

CRITICAL RULES:
1. Output ONLY raw markdown starting with YAML frontmatter (no ```markdown fences)
2. [[wikilinks]] must ONLY reference concepts within {module_code} — NEVER link to other modules
3. If a concept matches an existing note, use its exact name as a wikilink
4. Use LaTeX ($..$ for inline, $$...$$ for display) for all math
5. Use Obsidian callout boxes (> [!note], > [!warning], > [!tip]) for important points
6. Be comprehensive — include all definitions, formulas, code snippets, and examples from the source

Existing notes in {module_code} you can link to: {existing_notes_str}

Generate the note with this structure:

---
module: {module_code}
course: {course_name}
date: {today}
source: {filename}
tags: [{module_code.lower()}, lecture-notes, auto-generated]
up: "[[MOD_INDEX]]"
---

# {{title derived from content}}

> [!info] Navigation
> ↑ Back to [[MOD_INDEX]]

## Summary
3-5 sentence overview.

## Key Concepts
- [[ConceptName]] — definition (only link concepts within {module_code})

## Detailed Notes
Comprehensive structured notes with subheadings. Include all formulas, code, tables, diagrams-as-text.

## Worked Examples
Any examples or exercises from the material, with solutions.

## Exam Relevance
> [!warning] Exam Topics
> Bullet points of likely exam items.

---
Lecture material:
{all_text[:20000]}"""

            response = self.openai_client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            note_content = response.choices[0].message.content

            # Strip markdown code fences if GPT wraps them
            if note_content.startswith("```"):
                lines = note_content.split("\n")
                note_content = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])

            # Save note
            note_path = note_dir / f"{stem}.md"
            note_path.write_text(note_content, encoding="utf-8")
            logger.info(f"[V{VERSION}] Obsidian note saved: {note_path}")

            # Update MOD_INDEX.md (preferred) or index.md (fallback)
            mod_index_path = note_dir / "MOD_INDEX.md"
            index_path = note_dir / "index.md"
            target_index = mod_index_path if mod_index_path.exists() else index_path

            existing_content = ""
            if target_index.exists():
                existing_content = target_index.read_text(encoding="utf-8")

            link_line = f"- [[{stem}]]"
            if link_line not in existing_content:
                with open(target_index, "a", encoding="utf-8") as f:
                    if not existing_content:
                        f.write(f"# {course_name}\n\n## Auto-Generated Notes\n\n")
                    elif "## Auto-Generated Notes" not in existing_content:
                        f.write(f"\n## Auto-Generated Notes\n\n")
                    f.write(link_line + "\n")
                logger.info(f"[V{VERSION}] Added {stem} to {target_index.name}")

        except Exception as e:
            logger.error(f"[V{VERSION}] Obsidian note generation failed: {e}")

    @staticmethod
    def escape_md(text):
        """Escape special Markdown characters in dynamic content."""
        if not text:
            return ""
        for ch in ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']:
            text = text.replace(ch, f'\\{ch}')
        return text

    def process(self):
        try:
            logger.info(f"--- Starting Canvas Pipeline Version {VERSION} ---")
            
            # Check for Daily Digest (at 8 AM UTC/Local depending on runner)
            if datetime.now().hour == 8:
                self.send_daily_digest()

            courses = self.get_active_courses()

            for course in courses:
                course_id = course.get("id")
                course_name = course.get("name", "Unknown").replace("/", "-")

                # 1. Check for New Announcements
                announcements = self.get_announcements(course_id)
                for ann in announcements:
                    aid = f"ann_{ann.get('id')}"
                    if not self.is_item_seen(aid):
                        title = self.escape_md(ann.get("title", ""))
                        message = self.escape_md(ann.get("message", "")[:500]) + "\\.\\.\\."
                        logger.info(f"[V{VERSION}] New announcement: {ann.get('title')}")
                        msg = f"📢 *New Announcement: {self.escape_md(course_name)}*\n\n*Title:* {title}\n\n{message}\n\n[Open in Canvas]({ann.get('html_url')})"
                        telegram_send_message(msg)
                        self.mark_item_seen(aid)

                # 2. Check for New Assignments
                assignments = self.get_assignments(course_id)
                for ass in assignments:
                    asid = f"asgn_{ass.get('id')}"
                    # We check if created recently or if not seen
                    created_at = datetime.fromisoformat(ass.get("created_at").replace("Z", "+00:00"))
                    if created_at > (datetime.now(timezone.utc) - timedelta(hours=48)) and not self.is_item_seen(asid):
                        name = self.escape_md(ass.get("name", ""))
                        due = self.escape_md(str(ass.get("due_at", "N/A")))
                        logger.info(f"[V{VERSION}] New assignment: {ass.get('name')}")
                        msg = f"📝 *New Assignment: {self.escape_md(course_name)}*\n\n*Name:* {name}\n*Due:* {due}\n\n[View Assignment]({ass.get('html_url')})"
                        telegram_send_message(msg)
                        self.mark_item_seen(asid)

                # 3. Check for New Files (Original logic)
                files = self.get_course_files(course_id)
                for file_info in [f for f in files if f.get("filename", "").lower().endswith(".pdf")]:
                    fid = file_info.get("id")
                    if not self.is_item_seen(fid):
                        filename = file_info.get("filename")
                        logger.info(f"[V{VERSION}] New file: {filename}")
                        local_path = DATA_DIR / filename
                        DATA_DIR.mkdir(exist_ok=True)
                        with requests.get(file_info.get("url"), headers=self.headers, stream=True) as r:
                            with open(local_path, 'wb') as f:
                                for bc in r.iter_content(8192): f.write(bc)

                        all_text = self.extract_text(local_path)
                        summary = self.summarize_pdf(all_text)
                        self.generate_obsidian_note(all_text, filename, course_name)

                        telegram_send_pdf(local_path, course_name)
                        telegram_send_plain(f"📝 Summary ({filename})\n\n{summary}")

                        local_path.unlink()
                        self.mark_item_seen(fid)

            logger.info(f"--- Pipeline Finished Successfully ---")
        except Exception as e:
            telegram_notify_error(f"❌ *Canvas Pipeline V{VERSION} Error*\n\n{str(e)}")

if __name__ == "__main__":
    pipeline = CanvasPipeline()
    pipeline.process()
