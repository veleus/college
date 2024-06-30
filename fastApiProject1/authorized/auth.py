# main.py
from fastapi import Depends, HTTPException, status, APIRouter, Response
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from db import query_data
from authorized.login import get_login
from typing import Annotated


import secrets

security = HTTPBasic()
app = APIRouter()


@app.post("/login/")
def login(credentials: HTTPBasicCredentials = Depends(security)):
    user = get_login(query_data, credentials.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    is_correct_password = secrets.compare_digest(
        credentials.password, user.password
    )

    if not is_correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return {"username": user.login,
            'fio': user.fio}


@app.get("/users/me")
def read_current_user(username: Annotated[str, Depends(login)]):
    n = username
    return n
