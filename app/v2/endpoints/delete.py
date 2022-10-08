import json
from fastapi import APIRouter
from starlette.responses import JSONResponse
from app.v2.models import delete

router = APIRouter()


@router.delete("/", summary="delete media")
async def delete_route(data: delete.Delete):
    return JSONResponse(data.media_delete(), 200)
