FROM alpine

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories

RUN apk update && apk add python3 py3-pip gcc g++ python3-dev tzdata libxml2-dev libxslt-dev libxml2 libxslt \
    && pip3 install bilibili-api aiohttp -i https://pypi.tuna.tsinghua.edu.cn/simple

WORKDIR /app

COPY ./Monitor .

ENTRYPOINT ["python3", "Monitor"]