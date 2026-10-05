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
    """Create fictional research-administration documents for the demo."""

    documents = {
        "policies/conflict_of_interest_policy.txt": """
DOCUMENT ID: POLICY-COI-001
TITLE: Financial Conflict of Interest Policy
DOCUMENT TYPE: Policy
OWNER: Office of Research Administration
CLASSIFICATION: Internal
VERSION: 1.0
EFFECTIVE DATE: 2026-01-01
SOURCE: Synthetic demonstration data

PURPOSE

This policy establishes requirements for identifying, disclosing,
reviewing, and managing financial conflicts of interest associated
with sponsored research.

POLICY

Investigators participating in sponsored research must disclose
significant financial interests that could reasonably appear to
affect the design, conduct, reporting, or administration of research.

Disclosures must be submitted before participation in a new sponsored
research project and updated when relevant financial circumstances change.

Active sponsored projects may require review when a new financial
conflict is identified.

The Office of Research Administration will determine whether a
management plan, additional review, or other action is required.

If sufficient information is not available to determine whether a
conflict exists, the matter must be escalated for human review.
""",

        "grants/ai_clinical_decision_support.txt": """
DOCUMENT ID: GRANT-DOC-001
TITLE: AI-Assisted Clinical Decision Support
DOCUMENT TYPE: Grant
OWNER: Office of Research Administration
CLASSIFICATION: Internal
VERSION: 1.0
SOURCE: Synthetic demonstration data

PRINCIPAL INVESTIGATOR

Dr. Maya Chen
Department of Biomedical Engineering

PROJECT SUMMARY

The AI-Assisted Clinical Decision Support project investigates methods
for using machine learning to support clinical research workflows.

The project includes development and evaluation of artificial intelligence
models for research decision support.

SPONSOR

National Science Foundation

GRANT IDENTIFIER

GRANT-001

PROJECT STATUS

Active

AWARD AMOUNT

$450,000

COMPLIANCE NOTES

The project is subject to applicable institutional research policies,
including financial conflict-of-interest requirements.
""",

        "contracts/research_data_agreement.txt": """
DOCUMENT ID: CONTRACT-001
TITLE: Synthetic Research Data Use Agreement
DOCUMENT TYPE: Contract
OWNER: Office of Research Administration
CLASSIFICATION: Internal
VERSION: 1.0
SOURCE: Synthetic demonstration data

PURPOSE

This fictional agreement defines requirements for handling research
information used in collaborative projects.

DATA HANDLING

Research data classified as internal may only be accessed by authorized
project personnel.

Sensitive institutional data must not be transmitted to unauthorized
external services.

Any automated AI system processing protected information must enforce
applicable access controls and maintain source provenance.

Human review is required when contractual requirements are ambiguous.
""",

        "protocols/ai_research_protocol.txt": """
DOCUMENT ID: PROTOCOL-001
TITLE: AI Research Review Protocol
DOCUMENT TYPE: Protocol
OWNER: Research Compliance Office
CLASSIFICATION: Internal
VERSION: 1.0
SOURCE: Synthetic demonstration data

PURPOSE

This protocol defines review procedures for research projects using
artificial intelligence systems.

REVIEW REQUIREMENTS

Research teams must document:

- intended AI use
- source data
- access controls
- model provider
- data retention requirements
- human oversight procedures

Projects involving sensitive research information require confirmation
that institutional data is not exposed to unauthorized model providers.

Questions that cannot be resolved from available evidence must be
escalated to the appropriate research administrator.
""",

        "regulatory/sponsored_research_guidance.txt": """
DOCUMENT ID: REG-001
TITLE: Sponsored Research Compliance Guidance
DOCUMENT TYPE: Regulatory Guidance
OWNER: Research Compliance Office
CLASSIFICATION: Public
VERSION: 1.0
SOURCE: Synthetic demonstration data

OVERVIEW

Sponsored research projects must comply with applicable institutional,
sponsor, contractual, and regulatory requirements.

Research administrators should verify relevant compliance requirements
before approving significant project changes.

Potential conflicts of interest, data-use restrictions, and research
protocol requirements should be evaluated using authoritative source
documents.

Automated systems may assist with retrieval and analysis but should not
invent missing regulatory requirements.

When evidence is insufficient, the appropriate response is to identify
the limitation and escalate the issue for human review.
""",
    }

    for relative_path, content in documents.items():
        file_path = DOCUMENTS_DIR / relative_path

        file_path.parent.mkdir(parents=True, exist_ok=True)

        file_path.write_text(
            content.strip() + "\n",
            encoding="utf-8",
        )

        print(f"Created: {file_path}")


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
    insert_synthetic_data()
    create_documents()
    print("All synthetic demo data generated successfully.")    


if __name__ == "__main__":
    main()
