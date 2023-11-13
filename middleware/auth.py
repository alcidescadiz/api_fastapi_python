from typing import Annotated
from fastapi import FastAPI, Header, HTTPException, Request

async def middle_prueba(request: Request):
    
    print('hola print middleware')
    return 'hola'

async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key