from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse
from app.v2.models import upload
from app.v2.utils.auth import check_auth

router = APIRouter()


@router.post("/", summary="upload media")
async def upload_route(data: upload.Upload, dependencies=Depends(check_auth)):
    return JSONResponse(data.media_upload(), 200)
