FROM ubuntu:18.04
RUN apt update && apt upgrade -y && apt install sysbench -y
COPY bench.sh .
CMD ./bench.sh
