from fastapi import APIRouter

from controllers.http.v1.admin import router as admin_router

v1_router = APIRouter(prefix='/api/v1')

v1_router.include_router(admin_router)
