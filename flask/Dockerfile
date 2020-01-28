FROM python:3.7

ARG project_dir=/var/www/flask/

ADD ./requirements.txt $project_dir

WORKDIR $project_dir

RUN pip install -r requirements.txt