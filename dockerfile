FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential pkg-config && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip

COPY requirements.txt* .
RUN pip install uvicorn

RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD [ "uvicorn","main:app","--host","0.0.0.0","--port","8000" ]