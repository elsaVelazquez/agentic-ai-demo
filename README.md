# agentic-ai-demo
Agentic AI • RAG • AI Orchestration • Semantic Search • Secure AI • Human-in-the-Loop • AI Governance • Workflow Automation

Note: This repo uses strictly reproducible synthetic source data. The SQLite db is generated locally, not committed as a binary artifact to make the demo inspectable and reproducible while showcasing instructions dont need to expose PII or real data.

GitHub = code + schema + synthetic examples
Local runtime = generated DB + embeddings/vector store
Secrets = .env, never GitHub

```
                    ┌─────────────┐
                    │   SQLite    │
                    │ structured  │
                    │    data     │
                    └──────┬──────┘
                           │
                           │ exact lookup
                           │
User → API → Orchestration ┼────────→ LLM → Response
                           │
                           │ semantic retrieval
                           │
                    ┌──────▼──────┐
                    │   Qdrant    │
                    │   vectors   │
                    └──────▲──────┘
                           │
                     embeddings
                           │
                PDFs / policies / contracts
```

Document → Chunk →  Embedding →  Vector →  Qdrant collection →  Similarity search →  Relevant chunks →  LLM context


## → Knowledge Base = the corpus

- research administration and regulatory affairs documents
- structured + unstructured data
- synthetic data for testing
- source metadata
- permissions / ownership metadata

## → RAG = ingest → chunk → embed → store → retrieve

- Manage and scale vector databases to ensure high-speed semantic search
- ingestion pipeline
- document parsing
- chunking
- embeddings
- vector database
- semantic search
- retrieval
- retrieval inference
- orchestration
- automation candidates

## → Security = identity + access + data + model

- data sovereignty (AKA ontology)
- authentication
- authorization
- API security
- credentials / secrets
- PII
- IP
- institutional data
- LLM / API controls
- AI safety
- secure internal interface

## → Decision Logic + HITL = retrieve → reason → validate → answer OR escalate

- structured decision paths
- business rules
- confidence thresholds
- evidence / citations
- escalation
- human-in-the-loop review
- fallback behavior
- "I don't know" / insufficient evidence handling

## → Evaluate

- automated tests
- test cases
- hallucination checks
- retrieval accuracy
- answer accuracy
- groundedness
- latency
- cost
- productivity improvement
- corpus / source material

Workflow automation is a key component of the AI demo. It automates the retrieval and retrieval inference processes, allowing users to focus on the decision logic and HITL.
> First prove that RAG + orchestration works.  
> Then decide whether model optimization or fine-tuning is actually necessary.

## → Model Optimization

- model selection
- prompt / config tuning
- inference settings
- vLLM
- GPU usage
- HPC
- Slurm
- PEFT
- LoRA
- fine-tuning parameters

## → Document

- API documentation
- RAG configuration
- architecture
- user guides
- training documentation
- Accessibility — apply it to the UI
- deployment / scaling notes
- security assumptions
- known limitations

*** Layout ***
```
  agentic-ai-demo/
│
├── README.md
│
├── data/
│   ├── structured/
│   │   |── research_admin.db
    |   ├── schema.sql
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
└── .gitignore
```