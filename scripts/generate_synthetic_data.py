"Generate synthetic research-administration data for the AI demo."""
'''SQLite database + fictional research documents'''
'''Demo uses reproducible synthetic data and public data; no private institutional, client, PII, or proprietary information exposed.'''



import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
STRUCTURED_DIR = DATA_DIR / "structured"
DOCUMENTS_DIR = DATA_DIR / "documents"


def create_directories():
    """Create the folders needed for generated demo data."""
    STRUCTURED_DIR.mkdir(parents=True, exist_ok=True)
    DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)


def create_database():
    """Create the synthetic SQLite research-administration database."""
    pass


def create_documents():
    """Create fictional research-administration documents."""
    pass


def main():
    """Generate all synthetic demo data."""
    create_directories()
    create_database()
    create_documents()


if __name__ == "__main__":
    main()