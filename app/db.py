import os

import databases
from fastapi import FastAPI

DATABASE_URL = os.environ.get("DATABASE_URL")


async def connect_to_db(app: FastAPI) -> None:
    d = databases.Database(
        url=DATABASE_URL,
    )
    app.state.db = d


async def close_db_connection(app: FastAPI) -> None:
    if not app.state.db.is_connected:
        return
    await app.state.db.disconnect()
