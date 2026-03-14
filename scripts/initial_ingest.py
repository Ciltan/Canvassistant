import os
import json
import logging
import requests
import pdfplumber
from pathlib import Path
from concurrent import futures
from typing import List, Dict, Set
from openai import OpenAI
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv("backend/.env")

# Constants
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OBSIDIAN_API_KEY = "f9ba9cc41ba1598f6f9e356a69b610a10230962c31682351824dfca97136a375"
OBSIDIAN_BASE_URL = "https://127.0.0.1:27124"
DATA_DIR = Path("data")

client = OpenAI(api_key=OPENAI_API_KEY)

class ObsidianOrchestrator:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {OBSIDIAN_API_KEY}",
            "Content-Type": "text/markdown"
        }
        self.vault_topics: Set[str] = set()
        self.processed_log_path = Path("processed_files.json")
        self.processed_files = self._load_processed_log()

    def _load_processed_log(self) -> Dict:
        if self.processed_log_path.exists():
            with open(self.processed_log_path, 'r') as f:
                return json.load(f)
        return {"processed": []}

    def _save_processed_log(self):
        with open(self.processed_log_path, 'w') as f:
            json.dump(self.processed_files, f, indent=2)

    def fetch_vault_map(self):
        """Build a map of existing note titles to enable dense linking."""
        logger.info("Mapping Obsidian vault topics...")
        try:
            # We'll crawl the main directories we know exist
            folders = ["CG2111A", "CS2040C", "CS1231", "MA1508E", "DTK1234"]
            for folder in folders:
                resp = requests.get(f"{OBSIDIAN_BASE_URL}/vault/{folder}/", headers=self.headers, verify=False)
                if resp.status_code == 200:
                    files = resp.json().get("files", [])
                    for f in files:
                        if f.endswith(".md"):
                            topic = f.split("/")[-1].replace(".md", "")
                            self.vault_topics.add(topic)
                else:
                    logger.warning(f"Could not map folder {folder}: {resp.status_code}")
            logger.info(f"Vault map built with {len(self.vault_topics)} topics.")
        except Exception as e:
            logger.error(f"Failed to fetch vault map: {e}")

    def extract_text(self, pdf_path: Path) -> str:
        text = ""
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    content = page.extract_text()
                    if content:
                        text += content + "\n"
        except Exception as e:
            logger.error(f"Text extraction failed for {pdf_path}: {e}")
        return text

    def generate_note(self, text: str, filename: str, module_name: str) -> str:
        """Generate a Claude-style note using GPT-4o-mini."""
        logger.info(f"Generating Claude-style note for {filename}...")
        
        # Build a hint for linking based on vault topics
        topics_hint = ", ".join(list(self.vault_topics)[:50]) # Sample for context
        
        prompt = f"""Target Module: {module_name}
        Original File: {filename}
        
        Task: Convert the following lecture material into a premium, highly structured "Claude-style" Obsidian note.
        
        Strict Formatting Rules:
        1. Use YAML frontmatter with tags: [{module_name}, lecture-notes, academic].
        2. # Title: Clear, descriptive heading.
        3. ## Overview: A high-level executive summary (3-4 sentences).
        4. ## Key Concepts & Definitions: Use [[wikilinks]] for all technical terms. 
           - Existing topics to prioritize linking if relevant: {topics_hint}
        5. ## Detailed Technical Breakdown: Use subheadings, bullet points, and tables for clarity.
        6. ## Implementation/Examples (if applicable): Use triple-backtick code blocks.
        7. > [!note] / [!important] / [!warning]: Use at least 2 relevant callouts.
        8. ## Related: Link to other [[ModuleIndex]] or conceptual neighbors.

        Content:
        {text[:15000]} # Truncate to stay within context limits
        """

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert academic tutor that writes beautifully structured Obsidian notes. IMPORTANT: Output ONLY the raw markdown. Do NOT wrap the entire response in triple backticks (```markdown)."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1
            )
            content = response.choices[0].message.content
            # Handle cases where the LLM still wraps in backticks
            if content.startswith("```markdown"):
                content = content.replace("```markdown", "", 1)
            if content.startswith("```"):
                content = content.replace("```", "", 1)
            if content.endswith("```"):
                content = content[::-1].replace("```"[::-1], "", 1)[::-1]
            
            return content.strip()
        except Exception as e:
            logger.error(f"GPT summarization failed: {e}")
            return ""

    def upload_to_obsidian(self, content: str, module_folder: str, filename: str):
        stem = Path(filename).stem
        logger.info(f"Syncing {stem}.md (Length: {len(content)}, Preview: {content[:20]!r})")
        # Ensure module folder names are consistent with Obsidian structure
        clean_folder = module_folder.split(" ")[0].upper() # e.g. "CG2111A"
        url = f"{OBSIDIAN_BASE_URL}/vault/{clean_folder}/{stem}.md"
        
        try:
            resp = requests.put(url, headers=self.headers, data=content.encode('utf-8'), verify=False)
            if resp.status_code in [200, 201, 204]:
                logger.info(f"Successfully synced: {clean_folder}/{stem}.md")
                return True
            else:
                logger.error(f"Sync failed for {stem}: {resp.status_code} - {resp.text}")
                return False
        except Exception as e:
            logger.error(f"Obsidian sync error: {e}")
            return False

    def process_file(self, pdf_path: Path):
        file_key = str(pdf_path)
        if file_key in self.processed_files["processed"]:
            logger.info(f"Skipping already processed file: {pdf_path.name}")
            return

        full_module_name = pdf_path.parent.name
        module_code = full_module_name.split(" ")[0].upper() # Clean tag, e.g. "CG2111A"
        
        text = self.extract_text(pdf_path)
        if not text.strip():
            logger.warning(f"No text extracted from {pdf_path.name}. Skipping.")
            return

        note_content = self.generate_note(text, pdf_path.name, module_code)
        if note_content:
            if self.upload_to_obsidian(note_content, full_module_name, pdf_path.name):
                self.processed_files["processed"].append(file_key)
                self._save_processed_log()

    def run(self, max_workers=5, limit=None):
        self.fetch_vault_map()
        
        pdf_files = list(DATA_DIR.rglob("*.pdf"))
        # Filter out anything already processed to avoid double work
        unprocessed_pdf_files = [f for f in pdf_files if str(f) not in self.processed_files["processed"]]
        logger.info(f"Found {len(unprocessed_pdf_files)} unprocessed matching PDFs.")
        
        if limit:
            unprocessed_pdf_files = unprocessed_pdf_files[:limit]
            logger.info(f"Limited run: processing first {limit} files.")

        with futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(self.process_file, unprocessed_pdf_files)

if __name__ == "__main__":
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    orchestrator = ObsidianOrchestrator()
    # FULL RUN
    orchestrator.run()
