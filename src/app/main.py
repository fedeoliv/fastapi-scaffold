from typing import Annotated
from fastapi import Depends, FastAPI

from app.settings import Settings, get_settings

app = FastAPI()


@app.get("/")
async def root(settings: Annotated[Settings, Depends(get_settings)]):
    return {"message": "Hello World!"}
