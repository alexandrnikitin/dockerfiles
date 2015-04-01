FROM ubuntu:14.04

RUN apt-get -y update && \
    
    apt-get -y install curl && \
    curl -sL https://deb.nodesource.com/setup | sudo bash - && \
    apt-get -y install nodejs && \
    
    apt-get -y install git && \
    git clone https://github.com/etsy/statsd.git /src/statsd && \
    cd /src/statsd && \
    git checkout v0.7.2

CMD ["/usr/bin/node", "/src/statsd/stats.js", "/etc/statsd-config.js"]

EXPOSE 8125/udp 8126
