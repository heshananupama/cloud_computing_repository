FROM ubuntu:16.04

WORKDIR /app

ENV DEBIAN_FRONTEND noninteractive

RUN apt update -y && \
    apt install -y \
        wget unzip mysql-server apache2 php libapache2-mod-php php-mcrypt \
        php-mysql default-jdk python ssh sysstat dos2unix supervisor make

RUN wget https://github.com/uillianluiz/RUBiS/archive/master.zip && \
    unzip master.zip && \
    cp -r /app/RUBiS-master/PHP/ /var/www/html/ && \
    cd /app/RUBiS-master/Client/bench; chmod +x *.sh *.awk; dos2unix *.sh *.awk

COPY rubis.properties ./RUBiS-master/Client/rubis.properties
COPY run.sh .
RUN chmod +x run.sh

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD /usr/bin/supervisord