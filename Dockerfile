# pull official base image
FROM python:3.8.3-alpine
# set work directory

ENV PROJECT_DIR /internship_crm/

WORKDIR ${PROJECT_DIR}
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install psycopg2 dependencies
RUN apk update \
    && apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo postgresql-dev
# install dependencies
COPY Pipfile Pipfile.lock ${PROJECT_DIR}

RUN pip install --upgrade pip && pip install pipenv && pipenv install --system --deploy

# copy entrypoint.sh
COPY ./entrypoint.sh .
# copy project
COPY . .