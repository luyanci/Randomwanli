import os
import json
import random
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()
hoster = "https://randomwanli.zeabur.app"

def random_type():
    types=random.randint(1,3)
    if types == 1:
        return 'png'
    if types == 2:
        return 'gif'
    if types == 3:
        return 'jpg'

def get_end(type:str):
    if type == 'jpg':
        return 'jpeg'
    else:
        return type

def check_type(type:str):
    num_group=json.load(open("res/file.json",mode="r",errors="ignore"))
    return num_group[type]

@app.get("/")
#async def root():
#    return {"message": "Hello World"}
async def get_random():
    types=random_type()
    endnum=check_type(types)
    #print(endnum)
    num=random.randint(1,endnum)
    url=f"{hoster}/getwanli/{num}?types={str(types)}"
    return {"type":types,"url": url}

@app.get("/favicon.ico")
def get_favicon():
    return FileResponse("res/favicon.ico",media_type=f"image/icon")
    

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/getwanli/{filename}")
async def get_wanli(filename:str,types:Optional[str]=None):
    typeend=get_end(types)
    filepath= f"res/{types}/{filename}.{types}"
    print(filepath)
    if not os.path.exists(filepath):
        return {"code":404,"message":"Not Found!"}
    return FileResponse(filepath,media_type=f"image/{typeend}")