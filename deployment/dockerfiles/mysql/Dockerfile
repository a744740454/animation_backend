FROM mysql:5.7
ENV MYSQL_ROOT_PASSWORD=sadnesspineapple
ENV TZ=Asia/Shanghai
COPY init.sql /docker-entrypoint-initdb.d
CMD ["mysqld"]
