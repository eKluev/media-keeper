import os
import logging
import bugsnag
from fastapi import FastAPI
from app.v2.api import router as router_v2


def get_application() -> FastAPI:
    application = FastAPI(title="Media Keeper API", root_path="/", docs_url='/', redoc_url=None)
    if os.environ.get('BUGSNAG'):
        bugsnag.configure(api_key=os.environ.get('BUGSNAG'), project_root="/")
    else:
        logging.warning("Bugsnag isn't configured!")
    application.include_router(router_v2, tags=['2.0'], prefix='/v2')
    return application


app = get_application()
