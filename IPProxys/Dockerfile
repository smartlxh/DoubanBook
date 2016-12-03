FROM python:2.7
MAINTAINER lixianhai smartlxh@gmail.com
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install requests

RUN pip install gevent
COPY * /code/

ENTRYPOINT python IPProxys.py
