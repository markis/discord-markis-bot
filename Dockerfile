FROM python:3-alpine3.12
MAINTAINER m@rkis.cc
ENTRYPOINT [ "python3" ]
CMD [ "-m", "markis_bot" ]
WORKDIR /app

ENV DISCORD_ID=""
ENV DISCORD_TOKEN=""

# Install pip dependencies and avoid
# docker layer caching invalidation
ADD ./requirements.txt /app/
RUN apk add --update build-base && \
    pip install --no-cache --upgrade pip setuptools && \
    pip install -r requirements.txt && \
    apk del build-base

ADD . /app

