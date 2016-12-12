From python:2.7
MAINTAINER lixianhai smartlxh@gmail.com
ENV PYTHONUNBUFFERED 1
RUN mkdir /douban
WORKDIR /douban
RUN pip install scrapy
RUN pip install bs4
ADD *.cfg /douban/
RUN mkdir -p /douban/douban
WORKDIR /douban/douban
ADD ./douban/*.py /douban/douban/
RUN mkdir spiders
WORKDIR spiders
ADD ./douban/spiders/*.py /douban/douban/spiders/

WORKDIR /douban
ENTRYPOINT scrapy crawl douban
