from fastapi import FastAPI

from core.config import FastApiConfig
from controllers.http import router


def create_app(fastapi_conf: FastApiConfig, version: str) -> FastAPI:
    app = FastAPI(**fastapi_conf.model_dump(), version=version)

    app.include_router(router)

    return app