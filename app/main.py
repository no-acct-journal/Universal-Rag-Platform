from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import Settings, get_settings
from app.core.exception_handlers import register_exception_handlers
from app.core.logging import configure_logging
from app.core.middleware import TraceIdMiddleware
from app.db.runtime import get_engine
from app.services.background_jobs import BackgroundJobRunner


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings: Settings = app.state.settings
    settings.ensure_storage_dirs()
    app.state.engine = get_engine()
    try:
        yield
    finally:
        BackgroundJobRunner.shutdown()


def create_app() -> FastAPI:
    settings = get_settings()
    configure_logging(settings.log_level)

    app = FastAPI(title=settings.app_name, lifespan=lifespan)
    app.state.settings = settings
    allowed_origins = [item.strip() for item in settings.cors_allow_origins.split(",") if item.strip()]
    cors_kwargs: dict = {
        "allow_origins": allowed_origins,
        "allow_credentials": True,
        "allow_methods": ["*"],
        "allow_headers": ["*"],
    }
    if settings.app_env == "local":
        cors_kwargs["allow_origin_regex"] = r"https?://(localhost|127\.0\.0\.1)(:\d+)?"
    app.add_middleware(CORSMiddleware, **cors_kwargs)
    app.add_middleware(TraceIdMiddleware)
    app.include_router(api_router, prefix=settings.app_api_prefix)
    register_exception_handlers(app)
    return app


app = create_app()
