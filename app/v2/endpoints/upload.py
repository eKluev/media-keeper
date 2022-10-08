import json
from fastapi import APIRouter
from starlette.responses import JSONResponse
from app.v2.models import upload

router = APIRouter()


@router.post("/", summary="upload media")
async def upload_route(data: upload.Upload):
    return JSONResponse(data.media_upload(), 200)
