"""Generate synthetic research-administration data for the AI demo.

Creates a SQLite database and fictional research documents.

The demo uses reproducible synthetic data and public data only.
No private institutional, client, PII, or proprietary information is exposed.
"""

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

    database_path = STRUCTURED_DIR / "research_admin.db"

    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS researchers (
            researcher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grants (
            grant_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            principal_investigator_id INTEGER NOT NULL,
            sponsor TEXT NOT NULL,
            amount REAL NOT NULL,
            status TEXT NOT NULL,
            source_url TEXT,
            FOREIGN KEY (principal_investigator_id)
                REFERENCES researchers(researcher_id)
        )
    """)

    connection.commit()
    connection.close()


def create_documents():
    """Create fictional research-administration documents."""
    pass


def insert_synthetic_data():
    """Insert fictional researchers and grants into the database."""

    database_path = STRUCTURED_DIR / "research_admin.db"

    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    researchers = [
        (1, "Dr. Maya Chen", "Biomedical Engineering", "maya.chen@example.edu"),
        (2, "Dr. Daniel Brooks", "Computer Science", "daniel.brooks@example.edu"),
        (3, "Dr. Sofia Ramirez", "Public Health", "sofia.ramirez@example.edu"),
    ]

    grants = [
        (
            "GRANT-001",
            "AI-Assisted Clinical Decision Support",
            1,
            "National Science Foundation",
            450000,
            "Active",
            "https://example.org/grants/001",
        ),
        (
            "GRANT-002",
            "Secure Machine Learning Infrastructure",
            2,
            "Department of Energy",
            625000,
            "Pending",
            "https://example.org/grants/002",
        ),
        (
            "GRANT-003",
            "Community Health Analytics Initiative",
            3,
            "National Institutes of Health",
            780000,
            "Active",
            "https://example.org/grants/003",
        ),
    ]

    cursor.executemany(
        """
        INSERT OR REPLACE INTO researchers
        (researcher_id, name, department, email)
        VALUES (?, ?, ?, ?)
        """,
        researchers,
    )

    cursor.executemany(
        """
        INSERT OR REPLACE INTO grants
        (
            grant_id,
            title,
            principal_investigator_id,
            sponsor,
            amount,
            status,
            source_url
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        grants,
    )

    connection.commit()
    connection.close()

    print("Synthetic database records inserted.")


def main():
    """Generate all synthetic demo data."""
    create_directories()
    create_database()
    # create_documents()
    insert_synthetic_data()
    print("All synthetic demo data generated successfully.")    


if __name__ == "__main__":
    main()
