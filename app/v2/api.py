from fastapi import APIRouter
from app.v2.endpoints.upload import router as upload_router
from app.v2.endpoints.delete import router as delete_router


router = APIRouter()

router.include_router(upload_router)
router.include_router(delete_router)
