from app.api.routes.deliver import router as deliver_router
from app.api.routes.create_db import router as create_router
from app.api.routes.ports import router as ports_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(create_router, prefix="/create_db", tags=["create_db"])
router.include_router(ports_router, prefix="/ports", tags=["ports"])
router.include_router(deliver_router, prefix="/deliver", tags=["deliver"])
