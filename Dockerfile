FROM python:3.7-alpine3.14

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories

RUN pip3 install requests -i https://pypi.tuna.tsinghua.edu.cn/simple

WORKDIR /app

COPY ./Monitor .

ENTRYPOINT ["python3", "Monitor"]
