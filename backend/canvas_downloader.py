import os
import re
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

CANVAS_TOKEN = os.getenv("CANVAS_TOKEN")
CANVAS_BASE_URL = os.getenv("CANVAS_BASE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Available for future use

if not CANVAS_TOKEN or not CANVAS_BASE_URL:
    raise EnvironmentError("Missing CANVAS_TOKEN or CANVAS_BASE_URL in .env file.")

HEADERS = {"Authorization": f"Bearer {CANVAS_TOKEN}"}
DATA_DIR = Path(__file__).parent.parent / "data"


def sanitize_folder_name(name: str) -> str:
    """Remove characters that are invalid in folder names."""
    return re.sub(r'[<>:"/\\|?*]', "_", name).strip()


def get_active_courses() -> list[dict]:
    """Fetch all active courses for the authenticated user."""
    url = f"{CANVAS_BASE_URL}/api/v1/courses"
    params = {"enrollment_state": "active", "per_page": 100}
    courses = []

    while url:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        courses.extend(response.json())

        # Handle Canvas pagination via Link header
        url = None
        link_header = response.headers.get("Link", "")
        for part in link_header.split(","):
            if 'rel="next"' in part:
                url = part[part.index("<") + 1 : part.index(">")]
                params = {}  # params are embedded in the next URL
                break

    return courses


def get_course_files(course_id: int) -> list[dict]:
    """Fetch all files for a given course ID."""
    url = f"{CANVAS_BASE_URL}/api/v1/courses/{course_id}/files"
    params = {"per_page": 100}
    files = []

    while url:
        try:
            response = requests.get(url, headers=HEADERS, params=params)
            response.raise_for_status()
            files.extend(response.json())
        except requests.HTTPError as e:
            print(f"  [!] Could not fetch files (status {e.response.status_code}). Skipping.")
            return []

        url = None
        link_header = response.headers.get("Link", "")
        for part in link_header.split(","):
            if 'rel="next"' in part:
                url = part[part.index("<") + 1 : part.index(">")]
                params = {}
                break

    return files


def download_file(file: dict, dest_dir: Path) -> None:
    """Download a single file to the destination directory."""
    filename = file.get("filename", "unknown.pdf")
    download_url = file.get("url")

    if not download_url:
        print(f"  [!] No download URL for '{filename}'. Skipping.")
        return

    dest_path = dest_dir / filename

    if dest_path.exists():
        print(f"  [=] Already exists: {filename}")
        return

    print(f"  [↓] Downloading: {filename}")
    response = requests.get(download_url, headers=HEADERS, stream=True)
    response.raise_for_status()

    dest_dir.mkdir(parents=True, exist_ok=True)
    with open(dest_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"  [✓] Saved: {filename}")


def main():
    print("=== Canvas PDF Downloader ===\n")
    print(f"Base URL : {CANVAS_BASE_URL}")
    print(f"Data dir : {DATA_DIR.resolve()}\n")

    print("Fetching active courses...")
    courses = get_active_courses()

    if not courses:
        print("No active courses found.")
        return

    print(f"Found {len(courses)} active course(s).\n")

    for course in courses:
        course_id = course.get("id")
        course_name = course.get("name") or course.get("course_code") or f"course_{course_id}"
        folder_name = sanitize_folder_name(course_name)
        course_dir = DATA_DIR / folder_name

        print(f"[Course] {course_name} (ID: {course_id})")

        files = get_course_files(course_id)
        pdfs = [f for f in files if isinstance(f, dict) and f.get("filename", "").lower().endswith(".pdf")]

        if not pdfs:
            print("  No PDFs found.\n")
            continue

        print(f"  Found {len(pdfs)} PDF(s). Downloading to '{course_dir}'...")
        course_dir.mkdir(parents=True, exist_ok=True)

        for pdf in pdfs:
            try:
                download_file(pdf, course_dir)
            except Exception as e:
                print(f"  [!] Error downloading '{pdf.get('filename')}': {e}")

        print()

    print("=== Download complete ===")


if __name__ == "__main__":
    main()
