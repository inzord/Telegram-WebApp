import logging

from fastapi import FastAPI
import uvicorn
from tortoise.contrib.fastapi import register_tortoise

from backend.app.api import routes
from backend.app.core.settings import settings
from fastapi.middleware.cors import CORSMiddleware

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(routes.router)

register_tortoise(
    app,
    db_url=settings.sync_database_url,
    modules={"models": ["backend.app.models.users"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[f"{settings.get_vue_base_url}"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
