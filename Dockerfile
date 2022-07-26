FROM python:3.7.13-alpine3.15

WORKDIR /app

RUN mkdir video \
    && pip3 install requests colorama

COPY ./BiliLive.py .

ENTRYPOINT ["python3", "BiliLive.py", "-o", "/app/video", "-r"]