# UniversalRagPlatform

UniversalRagPlatform is an early-stage backend project for building a general-purpose RAG platform.

The project is just getting started. The current codebase mainly contains the initial FastAPI application structure, database base classes, and a few SQLAlchemy models for documents, document chunks, and ingestion jobs.

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Alembic
- Redis
- PostgreSQL
- Milvus / Zilliz

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r app\requirements.txt
```

## Run

The application entry point is:

```text
app/main.py
```

After the remaining API, configuration, and service modules are added, the app can be started with:

```powershell
uvicorn app.main:app --reload
```

## Status

This repository is still under initial development. More APIs, services, migrations, tests, and documentation will be added later.
