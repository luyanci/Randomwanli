import os
import random
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()
hoster = "https://randomwanli.zeabur.app"

def random_type():
    types=random.randint(1,2)
    if types == 1:
        return 'png'
    if types == 2:
        return 'gif'

def check_type(type=str):
    if type =='png':
        return 10
    if type =='gif':
        return 31


@app.get("/")
#async def root():
#    return {"message": "Hello World"}
async def get_random():
    types=random_type()
    endnum=check_type(types)
    #print(endnum)
    num=random.randrange(1,endnum,1)
    url=f"{hoster}/getwanli/{num}?q={str(types)}"
    return {"type":types,"url": url}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/getwanli/{filename}")
async def get_wanli(filename:str,q: Optional[str]=None):
    filepath= f"res/{q}/{filename}.{q}"
    if not os.path.exists(filepath):
        return {"code":404,"message":"Not Found!"}
    return FileResponse(filepath,media_type=f"image/{q}")