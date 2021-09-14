#FROM python:3.9-alpine
#ENV PYTHONUNBUFFERED 1
#WORKDIR /usr/src/code/f
#
#COPY . .
#
#
## set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
## install psycopg2 dependencies
#RUN apk update \
#    && apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo postgresql-dev
## install dependencies
#COPY Pipfile Pipfile.lock ${PROJECT_DIR}
#
#RUN pip install --upgrade pip && pip install pipenv && pipenv install --system --deploy
#
## copy entrypoint.sh
#
#RUN chmod +x ./entrypoint.sh
#
#CMD ["sh", "${PROJECT_DIR}entrypoint.sh"]

FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/code/

COPY . .

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip3 install pipenv && pipenv install --system --deploy --ignore-pipfile

RUN chmod +x ./entrypoint.sh

CMD ["sh", "/usr/src/code/entrypoint.sh"]