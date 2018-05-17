FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

WORKDIR /etc/apt
RUN git clone https://github.com/h4ppyy/docker_sources.list
RUN mv docker_sources.list/sources.list sources.list
RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs

WORKDIR /code
