# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt-get update
RUN apt-get install gcc -y
RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "./server/run.py"]