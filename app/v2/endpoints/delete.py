from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse
from app.v2.models import delete
from app.v2.utils.auth import check_auth

router = APIRouter()


@router.delete("/", summary="delete media")
async def delete_route(data: delete.Delete, dependencies=Depends(check_auth)):
    return JSONResponse(data.media_delete(), 200)
