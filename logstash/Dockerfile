FROM ubuntu:14.04
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://download.elasticsearch.org/logstash/logstash/packages/debian/logstash_1.4.2-1-2c0f5a1_all.deb -O /tmp/logstash.deb && \
    wget https://download.elasticsearch.org/logstash/logstash/packages/debian/logstash-contrib_1.4.2-1-efd53ef_all.deb -O /tmp/logstash-contrib.deb && \
    dpkg -i /tmp/logstash.deb ; \
    dpkg -i /tmp/logstash-contrib.deb ; \
    apt-get update && \
    apt-get -f -y install && \
    rm -rf /tmp/logstash.deb /tmp/logstash-contrib.deb

EXPOSE 5000/udp

ENTRYPOINT ["/opt/logstash/bin/logstash", "-f", "/etc/logstash.conf"]
CMD []