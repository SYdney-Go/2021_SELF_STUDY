FROM python:3.8.10-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDOWNWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt