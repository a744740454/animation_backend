FROM python:3.8.5-slim-buster

LABEL Author=yiboshi@bitorobotics.ltd

ADD ./sources.list /etc/apt/sources.list
ADD . /app
哦
ENV TZ=Asia/Shanghai
ENV ATP_env=prod

WORKDIR /app

RUN apt update -y \
  && pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install -r /app/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 9099

CMD ["python", "main.py"]