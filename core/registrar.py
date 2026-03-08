from typing import cast

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from starlette.middleware import _MiddlewareFactory as StarletteMiddlewareFactory
from that_depends.providers import DIContextMiddleware

from controllers.http import router
from core.config import FastApiConfig
from errors import BaseError
from ioc import Container


def create_app(fastapi_conf: FastApiConfig, version: str) -> FastAPI:
    app = FastAPI(**fastapi_conf.model_dump(), version=version)

    app.include_router(router)

    add_exception_handlers(app)

    return app


def add_middleware(app: FastAPI) -> None:
    app.add_middleware(cast(StarletteMiddlewareFactory, DIContextMiddleware), Container)


def add_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(BaseError)
    def add_base_error_handler(request: Request, exc: BaseError) -> JSONResponse:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'detail': str(exc)})
