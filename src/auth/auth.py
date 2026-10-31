from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None


@app.get("/tests/")
async def test_auth(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
