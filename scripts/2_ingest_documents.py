"""Ingest synthetic research-administration documents, preserve metadata, and chunk text for later vector database loading.
load documents
→ preserve metadata
→ chunk text
→ inspect chunks
→ later embed
→ later load into Qdrant

will output docs and chunk count, ex:
Loaded 5 documents.
Created 13 chunks.
"""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DOCUMENTS_DIR = BASE_DIR / "data" / "documents"


def load_documents():
    """Load text documents and basic source metadata."""

    documents = []

    for file_path in DOCUMENTS_DIR.rglob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        document = {
            "file_name": file_path.name,
            "document_type": file_path.parent.name,
            "source_path": str(file_path.relative_to(BASE_DIR)),
            "text": text,
        }

        documents.append(document)

    return documents


def chunk_text(text, chunk_size=500, overlap=100):
    """Split text into overlapping character-based chunks."""

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def create_chunks(documents):
    """Create chunks while preserving document metadata."""

    all_chunks = []

    for document in documents:
        chunks = chunk_text(document["text"])

        for index, chunk in enumerate(chunks):
            all_chunks.append(
                {
                    "chunk_id": f"{document['file_name']}-{index}",
                    "file_name": document["file_name"],
                    "document_type": document["document_type"],
                    "source_path": document["source_path"],
                    "text": chunk,
                }
            )

    return all_chunks


def main():
    documents = load_documents()
    chunks = create_chunks(documents)

    print(f"Loaded {len(documents)} documents.")
    print(f"Created {len(chunks)} chunks.")

    for chunk in chunks:
        print("\n" + "=" * 70)
        print(f"Chunk ID: {chunk['chunk_id']}")
        print(f"Type: {chunk['document_type']}")
        print(f"Source: {chunk['source_path']}")
        print("-" * 70)
        print(chunk["text"])


if __name__ == "__main__":
    main()