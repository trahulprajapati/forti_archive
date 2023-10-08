#FROM ubuntu:latest

#ENTRYPOINT ["top", "-b"]
FROM python:3.9.6-alpine
ARG workdir=/opt/app
ARG app=archive
RUN mkdir -p $workdir
ARG web=/opt/web
RUN mkdir -p $web/staticfiles
RUN mkdir -p $web/mediafiles

WORKDIR $workdir
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ../../requirements.txt .
RUN apk add --no-cache linux-headers g++

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add libffi-dev

COPY ../../. .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

RUN mkdir -p /var/www/dkr




