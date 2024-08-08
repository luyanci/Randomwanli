import os
import json
import random
from dotenv import load_dotenv
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import FileResponse,RedirectResponse


app = FastAPI()
hoster = "https://randomwanli.zeabur.app"
load_dotenv("./.env")
custom=str(os.environ["HOSTER"])
if len(str(custom)) >= 7:
    use_custom=True
    print("Custom enabled!")

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
async def get_random(returns:Optional[str]=None,type:Optional[str]=None):
    types=type
    if type is None or type not in ['jpg','png','gif']:
        types=random_type()
    endnum=check_type(types)
    num=random.randint(1,endnum)
    if use_custom is True:
        url=f"{custom}/getwanli/{num}?type={str(types)}"
    else:
        url=f"{hoster}/getwanli/{num}?type={str(types)}"
    if returns == '307':
        return RedirectResponse(url=url)
    else:
        return {"type":types,"url": url}

@app.get("/favicon.ico")
def get_favicon():
    return FileResponse("res/favicon.ico",media_type="image/icon")
    
@app.get("/getwanli/{filename}")
async def get_wanli(filename:str,type:Optional[str]=None):
    typeend=get_end(type)
    filepath= f"res/{type}/{filename}.{type}"
    if not os.path.exists(filepath):
        return FileResponse("res/404.png",media_type="image/png")
    return FileResponse(filepath,media_type=f"image/{typeend}")
