# agentic-ai-demo
Agentic AI • RAG • AI Orchestration • Semantic Search • Secure AI • Human-in-the-Loop • AI Governance • Workflow Automation

Note: This repo uses strictly reproducible synthetic source data or publicly available general data for demonstration purposes only. The SQLite db is generated locally, using benign names not connected to real people, not committed as a binary artifact to make the demo inspectable and reproducible while showcasing instructions dont need to expose PII or real data.

GitHub = code + schema + synthetic examples

Local runtime = generated DB + embeddings/vector store

Secrets = .env, never GitHub ()

# agentic-ai-demo

**Agentic AI • RAG • AI Orchestration • Semantic Search • Secure AI • Human-in-the-Loop • AI Governance • Workflow Automation**

A small, reproducible demonstration of a secure agentic AI architecture for research administration and regulatory affairs.

> **Data note:** This repository uses strictly reproducible synthetic source data or publicly available general data for demonstration purposes only. Synthetic names are fictional and are not intended to represent real people. No private institutional, client, PII, or proprietary information is required.
>
> The SQLite database and vector store are generated locally rather than committed as binary artifacts. This keeps the demo inspectable and reproducible while demonstrating how AI workflows can operate without exposing sensitive data.

**GitHub = code + schema + synthetic examples**

**Local runtime = generated database + embeddings + vector store**

**Secrets = `.env`, never GitHub**

---

## Architecture

```text
                            User
                              │
                              ▼
                     ┌─────────────────┐
                     │  Orchestration  │
                     └────────┬────────┘
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
        Structured Retrieval      Semantic Retrieval
                 │                         │
                 ▼                         ▼
        ┌────────────────┐        ┌────────────────┐
        │     SQLite     │        │     Qdrant     │
        │ structured data|        | vector search  |
        |    (ex: counts)│        │  (ex: info)    │
        └────────┬───────┘        └────────┬───────┘
                 │                         │
                 │ exact results           │ relevant chunks
                 │                         │
                 └────────────┬────────────┘
                              │
                              ▼
                       Context Assembly
                              │
                              ▼
                    Validation / HITL
                              │
                              ▼
                             LLM
                              │
                              ▼
                           Response
```

The orchestrator determines which retrieval path is appropriate for the request.

**Structured question → SQL**

Example: How many active grants does a researcher have?

**Semantic question → Vector retrieval**

Example: What policy governs conflicts of interest in sponsored research?

**Hybrid question → SQL + Vector retrieval**

Example: Does an active grant have requirements affected by the conflict-of-interest policy?

---

## → Knowledge Base = Corpus

The knowledge base contains the information available to the AI system.

### Structured data

- researchers
- grants
- sponsors
- statuses
- relationships

### Unstructured / semi-structured data

- research administration documents
- regulatory affairs documents
- grant documents
- policies
- contracts
- agreements
- protocols
- public regulatory guidance

### Metadata

- source
- document ID
- document type
- version
- effective date
- owner
- permissions
- classification
- ingestion timestamp

Synthetic data is used for testing and demonstration.

---

## → RAG

**RAG = Retrieval-Augmented Generation**

### Ingestion

```text
Source
→ Parse
→ Normalize
→ Chunk
→ Attach Metadata
→ Embed
→ Index
```

### Retrieval

```text
Query
→ Query Embedding
→ Search
→ Permission / Metadata Filter
→ Rank
→ Relevant Context
```

### Generation

```text
Retrieved Context
→ Prompt
→ LLM
→ Grounded Answer
→ Citation
→ Validation
```

Full conceptual flow:

```text
Document
→ Parse
→ Chunk
→ Embedding
→ Vector
→ Qdrant Collection
→ Similarity Search
→ Relevant Chunks
→ LLM Context
→ Grounded Response
```

Key components:

- ingestion pipeline
- document parsing
- chunking
- embeddings
- vector database
- semantic search
- retrieval
- ranking
- context assembly
- retrieval inference
- orchestration
- workflow automation

---

## → Agentic AI + Orchestration

The agentic layer coordinates tools and determines how a request should be processed.

```text
                    Agent / Orchestrator
                             │
                     decides what to do
                             │
             ┌───────────────┼───────────────┐
             ▼               ▼               ▼
            SQL          Vector DB        API / Tool
             │               │               │
             └───────────────┼───────────────┘
                             ▼
                          Evidence
                             │
                             ▼
                          Reasoning
                             │
                             ▼
                  Answer / HITL / Action
```

The goal is not simply to call an LLM. The system selects appropriate tools and data sources, retrieves evidence, validates results, and determines whether to answer, take an allowed action, or escalate to a human.

---

## → Security + Governance

**Security = identity + access + data + model**

- authentication
- authorization
- role-based access control
- document-level permissions
- API security
- credentials / secrets
- PII protection
- intellectual property protection
- institutional data protection
- encryption
- data classification
- auditability
- source provenance
- data sovereignty
- LLM / API boundaries
- AI safety
- secure internal interfaces

### Data Sovereignty

Data sovereignty concerns where institutional data resides, who controls it, which systems or providers may receive it, applicable governance requirements, retention, and jurisdiction.

RAG alone does **not** make an AI system secure.

Authorization should occur before retrieval, document permissions should propagate into retrieval metadata, and only authorized context should be provided to an LLM.

### Ontology

Ontology is separate from data sovereignty.

It describes concepts and relationships within the domain.

```text
Researcher
    │
    └── principal investigator for ──→ Grant
                                         │
                                         ├── sponsored by ──→ Sponsor
                                         │
                                         └── governed by ──→ Policy
```

---

## → Decision Logic + HITL

**Retrieve → Reason → Validate → Answer OR Escalate**

- structured decision paths
- business rules
- confidence thresholds
- evidence
- citations
- escalation
- human-in-the-loop review
- fallback behavior
- insufficient-evidence handling
- "I don't know" behavior

Human review remains available for high-impact, ambiguous, low-confidence, or policy-sensitive decisions.

---

## → Evaluation

Retrieval and generation should be evaluated separately so failures can be isolated.

### Retrieval evaluation

- retrieval accuracy
- relevance
- ranking quality
- metadata filtering
- permission enforcement

### Generation evaluation

- answer accuracy
- groundedness
- hallucination checks
- citation accuracy
- insufficient-evidence behavior

### System evaluation

- automated tests
- test cases
- latency
- cost
- security
- accessibility
- productivity improvement
- corpus / source quality

> First prove that retrieval + RAG + orchestration work.
>
> Then determine whether model optimization or fine-tuning is actually necessary.

---

## → Workflow Automation

Workflow automation can automate repeatable retrieval and information-processing steps while keeping consequential decision logic subject to explicit rules and human review.

Potential automation candidates include:

- document ingestion
- metadata extraction
- document classification
- policy retrieval
- grant status lookup
- evidence collection
- routing
- notification
- escalation

---

## → Model Optimization

Model optimization comes **after** the retrieval architecture has been validated.

- model selection
- prompt / configuration tuning
- inference settings
- vLLM
- GPU usage
- HPC
- Slurm
- PEFT
- LoRA
- fine-tuning parameters

Fine-tuning should solve an identified model problem rather than compensate for poor retrieval, weak source data, or incorrect orchestration.

---

## → Documentation

- API documentation
- RAG configuration
- architecture
- data sources
- metadata schema
- security assumptions
- access-control assumptions
- user guides
- training documentation
- accessibility requirements
- deployment / scaling notes
- evaluation methodology
- known limitations

---

## Repository Layout

```text
agentic-ai-demo/
│
├── README.md
│
├── data/
│   ├── structured/
│   │   ├── research_admin.db      # generated locally
│   │   └── schema.sql
│   │
│   └── documents/
│       ├── policies/
│       ├── grants/
│       ├── contracts/
│       ├── protocols/
│       └── regulatory/
│
├── scripts/
│   └── generate_synthetic_data.py
│
├── src/
│
├── tests/
│
├── requirements.txt
├── .env                           # local only — never commit
└── .gitignore
```

---

## Current Build Progress

```text
✓ Repository structure
✓ Synthetic data strategy
✓ SQLite schema
✓ Synthetic structured data
✓ Security / provenance statement

NEXT
↓
Synthetic documents
↓
Document metadata
↓
Ingestion
↓
Parsing
↓
Chunking
↓
Embeddings
↓
Qdrant
↓
Retrieval evaluation
↓
LLM integration
↓
SQL + vector orchestration
↓
Validation + citations + HITL
↓
Optional public API / live data ingestion
```

### Development Principle

```text
Corpus first
    ↓
Retrieval second
    ↓
Model third
    ↓
Agent / orchestration fourth
```

The initial implementation validates retrieval independently before introducing generation. This makes it possible to distinguish retrieval failures from model reasoning or hallucination failures.