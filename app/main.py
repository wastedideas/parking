from typing import Callable

from fastapi import FastAPI

from app.db import close_db_connection, connect_to_db
from app.routes import router


def create_start_app_handler(fast_api_app: FastAPI) -> Callable:
    async def start_app() -> None:
        await connect_to_db(fast_api_app)

    return start_app


def create_stop_app_handler(fast_api_app: FastAPI) -> Callable:
    async def stop_app() -> None:
        await close_db_connection(fast_api_app)

    return stop_app


def get_application() -> FastAPI:
    application = FastAPI(title="Parking")

    application.add_event_handler("startup", create_start_app_handler(application))
    application.add_event_handler("shutdown", create_stop_app_handler(application))
    application.include_router(router)
    return application


app = get_application()
