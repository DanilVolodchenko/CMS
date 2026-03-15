import json

from loguru._logger import Logger
from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp


class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware for logging request-response."""

    def __init__(self, app: ASGIApp, logger: Logger, dispatch: DispatchFunction | None = None) -> None:
        super().__init__(app, dispatch)
        self._logger = logger

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:

        request_body = await request.body()
        try:
            body_json = json.loads(request_body)
            request_body_str = json.dumps(body_json, ensure_ascii=False)
        except json.JSONDecodeError:
            request_body_str = request_body.decode(encoding='utf-8')

        self._logger.info(
            '{host}:{port} —> {method} {path} — {body}',
            host=request.client.host,  # type: ignore[unresolved-attribute]
            port=request.client.port,  # type: ignore[unresolved-attribute]
            method=request.method,
            path=request.url.path,
            body=request_body_str or 'NO BODY',
        )

        response = await call_next(request)

        body = b''
        async for chunk in response.body_iterator:  # type: ignore[unresolved-attribute]
            body += chunk

        try:
            body_json = json.loads(body)
            response_body_str = json.dumps(body_json, ensure_ascii=False)
        except json.JSONDecodeError:
            response_body_str = body.decode(encoding='utf-8')

        self._logger.success(
            '{host}:{port} <— {method} {path} {status} — {body}',
            host=request.client.host,  # type: ignore[unresolved-attribute]
            port=request.client.port,  # type: ignore[unresolved-attribute]
            method=request.method,
            path=request.url.path,
            status=response.status_code,
            body=response_body_str or 'NO BODY',
        )

        return Response(
            content=body,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type,
        )
