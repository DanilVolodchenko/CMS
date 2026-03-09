from typing import cast

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from starlette.middleware import _MiddlewareFactory as StarletteMiddlewareFactory
from that_depends import Provide, inject
from that_depends.providers import DIContextMiddleware

from controllers.http import router
from core.config import FastApiConfig
from errors import BaseError
from infrastructure.builder import Builder
from infrastructure.components import footer, header, main
from infrastructure.generators import container, dataclass, forward_ref, pydantic
from ioc import Container


def create_app(fastapi_conf: FastApiConfig, version: str) -> FastAPI:
    app = FastAPI(**fastapi_conf.model_dump(), version=version)

    app.include_router(router)

    add_exception_handlers(app)

    collect_builder()

    return app


def add_middleware(app: FastAPI) -> None:
    app.add_middleware(cast(StarletteMiddlewareFactory, DIContextMiddleware), Container)


def add_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(BaseError)
    def add_base_error_handler(request: Request, exc: BaseError) -> JSONResponse:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'detail': str(exc)})


@inject
def collect_builder(builder: Builder = Provide[Container.builder]) -> None:
    builder.add_components(
        main.MainComponent,
        footer.FooterComponent,
        header.HeaderComponent,
    )
    builder.add_generators(
        container.ContainerGenerator,
        dataclass.DataclassGenerator,
        forward_ref.ForwardRefGenerator,
        pydantic.PydanticGenerator,
    )
