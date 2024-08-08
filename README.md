<div align="center">

<img src="https://randomwanli.zeabur.app/?returns=307" width=200 height=200>

~~(没想到吧，这里也是随机的)~~

# 随机梨梨(RandomLili)

[![Deployed on Zeabur](https://zeabur.com/deployed-on-zeabur-dark.svg)](https://zeabur.com?referralCode=luyanci&utm_source=luyanci)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/Fastapi-005571?style=for-the-badge&logo=fastapi&logoColor=white)
![docker](https://img.shields.io/badge/docker-0db7ed?style=for-the-badge&logo=docker&logoColor=white)
![github action](https://img.shields.io/badge/github%20action-000000?style=for-the-badge&logo=github-actions&logoColor=blue)


</div>

## 使用

### API地址

|部署平台|链接|
|-|-|
|Vercel|[https://randomwanli.vercel.app/](https://randomwanli.vercel.app/)|
|Zeabur|[https://randomwanli.zeabur.app/](https://randomwanli.zeabur.app/)|

### html

```html
<img src="https://randomwanli.zeabur.app/?returns=307">
```

### markdown

```md
![randomwanli](https://randomwanli.zeabur.app/?returns=307)
```

## API

|link|备注|
|-|-|
|/|随机获取一张图片（默认返回json，可307跳转）|
|/favicon.ico|-|
|/getwanli/{filename}|获取图片|

<details>

<summary>参数</summary>

#### /
|参数|可填写内容|备注|
|-|-|-|
|returns|307/-|返回方式，默认返回json文本|
|type|jpg/png/gif|获取图片类型，只能选一个|
|-|-|所有参数均可选，可无需填写|

#### /getwanli

|参数|填写内容|备注|
|-|-|-|
|filename|-|文件名|
|type|jpg/png/gif|获取图片类型，只能选一个|
|-|-|所有参数必须填写,否则抛一张404图片|

</details>

## 源代码使用/开发

```sh
~$ git clone https://github.com/luyanci/randomlili
~$ cd randomlili

~/randomlili$ pip install -r requirements.txt
~/randomlili$ uvicorn main:app --host 0.0.0.0 --reload
```

## 致谢

- 使用模板：[Zeabur FastAPI Template](https://zeabur.com/templates/MK8U02) 
    - 作者:[@MichaelYuhe](https://github,com/MichaelYuhe)
- 404图片：[SAWARATSUKI/KawaiiLogos](http://github.com/SAWARATSUKI/KawaiiLogos) 
