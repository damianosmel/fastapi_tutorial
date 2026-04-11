from fastapi import FastAPI
from app.api import ping,notes
from app.db import database, engine, metadata
import asyncio
from sqlalchemy import exc

app = FastAPI()


@app.on_event("startup")
async def startup():
    for _ in range(20):  # ~20 seconds total
        try:
            await database.connect()
            # run metadata.create_all in threadpool since it's blocking I/O
            await asyncio.get_running_loop().run_in_executor(None, metadata.create_all, engine)
            return
        except (exc.OperationalError, ConnectionError):
            await asyncio.sleep(1)
    raise RuntimeError("Could not connect to the database after retries")

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(ping.router)
app.include_router(notes.router, prefix="/notes", tags=['notes'])