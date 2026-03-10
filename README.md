# Canvas Study AI

AI-powered study assistant for NUS Canvas. Pulls your course PDFs, indexes them with embeddings, and lets you query them through a Chrome extension.

## Architecture

```
Canvassistant/
├── backend/
│   ├── main.py               ← FastAPI server
│   ├── canvas_downloader.py  ← Syncs PDFs from Canvas API
│   ├── ingest.py             ← Chunks + embeds PDFs into ChromaDB
│   ├── rag.py                ← RAG pipeline (query, topics, practice, summary)
│   ├── .env                  ← API keys (not committed)
│   └── requirements.txt
├── extension/
│   ├── public/manifest.json  ← Chrome Extension Manifest V3
│   ├── src/
│   │   ├── App.jsx           ← 4-tab UI (Chat, Topics, Practice, Summary)
│   │   ├── main.jsx
│   │   └── index.css
│   └── dist/                 ← Built extension (load this in Chrome)
└── data/                     ← Downloaded PDFs, organized by course
```

---

## Setup & Run

### 1. Configure API Keys

Edit `backend/.env`:

```env
CANVAS_API_TOKEN=your_canvas_token_here
CANVAS_BASE_URL=https://canvas.nus.edu.sg
OPENAI_API_KEY=your_openai_key_here
```

**Getting your Canvas API token:**
1. Log in to [canvas.nus.edu.sg](https://canvas.nus.edu.sg)
2. Go to **Account → Settings**
3. Scroll to **Approved Integrations** → click **+ New Access Token**
4. Copy the token into your `.env`

---

### 2. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

---

### 3. Download Canvas Files

```bash
cd backend
python canvas_downloader.py
```

This will download all PDFs from your active courses into `data/{course_name}/`.

---

### 4. Ingest & Index PDFs

```bash
cd backend
python ingest.py
```

This reads all PDFs, chunks them, embeds with OpenAI `text-embedding-3-small`, and stores in ChromaDB at `backend/chroma_db/`.

---

### 5. Start the Backend Server

```bash
cd backend
uvicorn main:app --reload --port 8000
```

API will be available at `http://localhost:8000`.

**Endpoints:**
| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Health check |
| GET | `/courses` | List indexed courses |
| POST | `/query` | Free-form Q&A with sources |
| POST | `/topics` | Identify likely exam topics |
| POST | `/practice` | Generate practice questions |
| POST | `/summarize` | Summarize a course |

---

### 6. Build & Load Chrome Extension

```bash
cd extension
npm install
npm run build
```

Then in Chrome:
1. Go to `chrome://extensions/`
2. Enable **Developer mode** (top right)
3. Click **Load unpacked**
4. Select the `extension/dist` folder
5. The extension icon will appear in your toolbar — click it to open!

> **Note:** You'll need to add icon images (`icon16.png`, `icon48.png`, `icon128.png`) to `extension/public/` for the extension to show a proper icon. You can use any 🎓 emoji-style icon or generate them.

---

## Tech Stack

- **Backend:** Python, FastAPI, uvicorn
- **RAG:** LangChain + ChromaDB + OpenAI GPT-4o-mini
- **Embeddings:** OpenAI text-embedding-3-small
- **Frontend:** React 19 + Vite 6 (Chrome Extension Manifest V3)
- **Canvas API:** REST API with token auth
