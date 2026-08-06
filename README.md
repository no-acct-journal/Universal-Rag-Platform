# UniversalRagPlatform

UniversalRagPlatform is an early-stage backend scaffold for a general-purpose RAG platform. The project is just getting started, so many application modules, APIs, services, migrations, tests, and runtime integrations still need to be added.

At the moment, the repository mainly contains the initial FastAPI entry point, SQLAlchemy database foundation, and core data models for documents, document chunks, and ingestion jobs.

## Current Status

Implemented so far:

- FastAPI application entry point in `app/main.py`
- SQLAlchemy declarative base in `app/db/base.py`
- Cross-database SQLAlchemy type helpers in `app/db/types.py`
- Initial ORM models in `app/models/`
- Python dependency list in `app/requirements.txt`

Not yet complete:

- API route modules
- Application configuration module
- Logging, middleware, and exception handling modules
- Service layer implementation
- Database migrations
- Document ingestion pipeline
- Vector database integration logic
- Tests and CI workflow

`app/main.py` already references future modules such as `app.api`, `app.core`, and `app.services`. Those modules are not present yet, so the app is not expected to run successfully until they are implemented or the entry point is adjusted.

## Tech Stack

- Python 3.11+
- FastAPI
- Uvicorn
- SQLAlchemy 2.x
- Alembic
- PostgreSQL / SQLite-compatible model types
- Redis
- PyMuPDF
- python-docx
- openpyxl
- Milvus / Zilliz SDK

## Project Structure

```text
.
└── app/
    ├── main.py
    ├── requirements.txt
    ├── db/
    │   ├── base.py
    │   └── types.py
    └── models/
        ├── document.py
        ├── document_chunk.py
        ├── ingestion_job.py
        └── mixins.py
```

## Local Development

From the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r app\requirements.txt
```

After the missing `app.api`, `app.core`, and `app.services` modules are implemented, the development server can be started with:

```powershell
uvicorn app.main:app --reload
```

Default local address:

```text
http://127.0.0.1:8000
```

## Environment Variables

Local configuration should be stored in `.env`. The file is intentionally ignored by Git.

Example values for future configuration:

```env
APP_ENV=local
APP_NAME=UniversalRagPlatform
DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/universal_rag
REDIS_URL=redis://localhost:6379/0
CORS_ALLOW_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

The exact environment variables should be finalized when the application configuration module is added.

## Data Model Overview

- `Document`: stores document metadata, source information, lifecycle status, access metadata, tags, and custom metadata.
- `DocumentChunk`: stores parsed document chunks, page or sheet positions, contextual text, vector IDs, and chunk-level metadata.
- `IngestionJob`: stores ingestion job state, current processing step, retry count, error details, and timestamps.

## Planned Work

1. Add the application configuration module.
2. Add logging, middleware, and exception handling.
3. Add API routers and a health check endpoint.
4. Add Alembic configuration and the first database migration.
5. Implement document upload, parsing, chunking, and ingestion services.
6. Integrate vector storage.
7. Add tests for models, configuration, and core API behavior.
8. Add development and deployment documentation as the project matures.
