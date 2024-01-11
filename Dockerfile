FROM python:3.7.13-alpine3.15

WORKDIR /app

RUN mkdir video \
    && pip3 install requests colorama

COPY ./biliLive .

ENTRYPOINT ["python3", "bililive", "-o", "/app/video", "-r"]
