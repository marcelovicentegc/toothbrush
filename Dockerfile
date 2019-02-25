FROM python:3.6.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /code
COPY /project/requirements/base.txt /code/
RUN pip install -r base.txt

COPY . /code/
