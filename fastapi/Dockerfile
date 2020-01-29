FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

RUN pip install fastapi

ARG project_dir=/var/www/fastapi/

ADD ./requirements.txt $project_dir

WORKDIR $project_dir

RUN pip install -r requirements.txt