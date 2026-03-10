"""
ingest.py — Reads PDFs from data/, chunks them, embeds with OpenAI, and stores in ChromaDB.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATA_DIR = Path(__file__).parent.parent / "data"
CHROMA_DIR = Path(__file__).parent / "chroma_db"


def load_pdfs() -> list:
    """Walk data/ and load all PDFs, attaching course_name metadata."""
    documents = []

    if not DATA_DIR.exists():
        print(f"[!] Data directory '{DATA_DIR}' does not exist. Run canvas_downloader.py first.")
        return documents

    for course_folder in sorted(DATA_DIR.iterdir()):
        if not course_folder.is_dir():
            continue

        course_name = course_folder.name
        pdf_files = list(course_folder.glob("*.pdf"))

        if not pdf_files:
            print(f"  [–] No PDFs in '{course_name}'")
            continue

        print(f"[Course] {course_name} — {len(pdf_files)} PDF(s)")

        for pdf_path in sorted(pdf_files):
            print(f"  [→] Loading: {pdf_path.name}")
            try:
                loader = PyPDFLoader(str(pdf_path))
                pages = loader.load()

                for page in pages:
                    page.metadata["course_name"] = course_name
                    page.metadata["file_name"] = pdf_path.name
                    page.metadata["page_number"] = page.metadata.get("page", 0) + 1

                documents.extend(pages)
            except Exception as e:
                print(f"  [!] Error loading '{pdf_path.name}': {e}")

    return documents


def chunk_documents(documents: list) -> list:
    """Split documents into smaller chunks for embedding."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    chunks = splitter.split_documents(documents)
    print(f"\n[✓] Split {len(documents)} pages into {len(chunks)} chunks.")
    return chunks


def embed_and_store(chunks: list) -> None:
    """Embed chunks using OpenAI and store in ChromaDB."""
    if not chunks:
        print("[!] No chunks to embed.")
        return

    print(f"\n[→] Embedding {len(chunks)} chunks with text-embedding-3-small...")

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        openai_api_key=OPENAI_API_KEY,
    )

    # Create / overwrite the ChromaDB vector store
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR),
        collection_name="canvas_docs",
    )

    print(f"[✓] Stored {len(chunks)} chunks in ChromaDB at '{CHROMA_DIR}'.")
    return vectorstore


def main():
    print("=== Canvas PDF Ingestion Pipeline ===\n")

    # Step 1: Load PDFs
    documents = load_pdfs()
    if not documents:
        print("\nNo documents found. Make sure you've run canvas_downloader.py first.")
        return

    print(f"\n[✓] Loaded {len(documents)} pages total.\n")

    # Step 2: Chunk
    chunks = chunk_documents(documents)

    # Step 3: Embed & Store
    embed_and_store(chunks)

    print("\n=== Ingestion complete ===")


if __name__ == "__main__":
    main()
