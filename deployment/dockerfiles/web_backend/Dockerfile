FROM python:3.8.5-slim-buster

LABEL Author=yiboshi@bitorobotics.ltd

ADD ./deployment/dockerfiles/web_backend/sources.list /etc/apt/sources.list
ADD . /app
ENV TZ=Asia/Shanghai
ENV ATP_env=prod

WORKDIR /app

RUN RUN sed -i "s@/archive.ubuntu.com/@/mirrors.163.com/@g" /etc/apt/sources.list \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get update --fix-missing -o Acquire::http::No-Cache=True \
    && pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install -r /app/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD ["python", "main.py"]