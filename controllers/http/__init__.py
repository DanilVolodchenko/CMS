from fastapi import APIRouter
from that_depends.integrations.fastapi import create_fastapi_route_class

from controllers.http.v1 import v1_router

# my_route_class = create_fastapi_route_class()
router = APIRouter()

router.include_router(v1_router)
