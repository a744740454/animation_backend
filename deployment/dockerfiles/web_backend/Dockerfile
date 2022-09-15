FROM python:3.8.5-slim-buster

LABEL Author=yiboshi@bitorobotics.ltd

ADD ./deployment/dockerfiles/web_backend/sources.list /etc/apt/sources.list
ADD . /app
ENV TZ=Asia/Shanghai
ENV ATP_env=prod

WORKDIR /app

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install -r /app/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD ["python", "main.py"]