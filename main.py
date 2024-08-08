import os
import json
import random
from dotenv import load_dotenv
from typing import Optional
from loguru import logger

from fastapi import FastAPI,HTTPException
from fastapi.responses import FileResponse,RedirectResponse

app = FastAPI()
use_custom=True
hoster = "https://randomwanli.zeabur.app" #默认域名
load_dotenv("./.env")
try:
    #读取自定义域名
    custom=str(os.environ["HOSTER"])
except:
    #如果失败，默认关闭自定义域名
    use_custom=False
finally:
    if use_custom is True and len(str(custom)) >= 7:
        hoster=custom
        logger.info("Custom enabled!")

def random_type():
    """
    随机返回图片类型
    """
    types=random.randint(1,3)
    return ['png', 'gif', 'jpg'][types - 1]

def get_end(type:str):
    if type == 'jpg':
        return 'jpeg'
    return type

def check_type(type:str):
    num_group=json.load(open("res/file.json",mode="r",errors="ignore"))
    return num_group[type]

@app.get("/")
async def get_random(returns:Optional[str]=None,type:Optional[str]=None):
    """
    返回随机图片(默认json文本,可307)
    """
    logger.info(f"Inputs: type:{type},returns:{returns}")
    types=type
    if type is None or type not in ['jpg','png','gif']:
        types=random_type()
    endnum=check_type(types)
    num=random.randint(1,endnum)
    url=f"{hoster}/getwanli/{num}?type={str(types)}"
    if returns == '307':
        return RedirectResponse(url=url)
    return {"type":types,"url": url}

@app.get("/favicon.ico")
def get_favicon():
    """
    favicon
    """
    return FileResponse("res/favicon.ico",media_type="image/icon")

@app.get("/getwanli/{filename}")
async def get_wanli(filename:str,type:Optional[str]=None):
    """
    返回指定图片
    """
    logger.info(f"filename:{filename},type:{type}")
    failed=False
    try:
        #因为图片文件名都是数字，所以试图转int
        int(filename)
    except Exception as e:
        #如果失败，则返回500的图片
        failed=True
        logger.warning(e)
    finally:
        if failed is True:
            return FileResponse("res/500.png",media_type="image/png")
    #特殊符号拒绝
    refuse_dict=['$','%','&','#','@','!','*','(',')','[',']','{','}','|','\\','/','?','<','>','=','+','-','_','~','^','`','\n','\r','\t','\b','\f','\v','\a','\b','\n','\r','\t','\b','\f','\v']
    if any(i in filename for i in refuse_dict) or any(i in type for i in refuse_dict):
        #如果参数包含特殊符号，则返回500的图片
        return FileResponse("res/500.png",media_type="image/png")
    if type is None or type not in ['jpg','png','gif']:
        #如果参数为空或者不在指定类型中，则返回404的图片
        return FileResponse("res/404.png",media_type="image/png")
    typeend=get_end(type)
    filepath= f"res/{type}/{filename}.{type}"
    try:
        if not os.path.exists(filepath):
            return FileResponse("res/404.png",media_type="image/png")
        return FileResponse(filepath,media_type=f"image/{typeend}")
    except:
        raise HTTPException(status_code=403, detail="Not Allowed")

@app.get("/getwanli")
def jump_to_root():
    """
    直接跳转api根
    """
    return RedirectResponse(url=f"{hoster}")

if __name__ == "__main__":
    #程序主函数
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)