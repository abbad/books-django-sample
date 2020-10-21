FROM python:3.6.8-jessie
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y \
    build-essential
RUN pip install --upgrade pip
RUN mkdir -p /code
COPY requirements.txt /
RUN pip install -r requirements.txt
WORKDIR /code
