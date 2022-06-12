FROM python:3

ENV PYTHONBUFFERED=1

RUN useradd -ms /bin/bash docker-user

WORKDIR /projekt

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./projekt/ .

RUN chown -R docker-user:docker-user /projekt

USER docker-user
