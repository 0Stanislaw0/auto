FROM python:3.6.13

MAINTAINER Stanislaw

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/auto

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

