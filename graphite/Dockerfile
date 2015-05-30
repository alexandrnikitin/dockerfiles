FROM     ubuntu:14.04.1

# Install prerequisites
RUN apt-get -y update && \
  apt-get -y \
  install python-dev \
  python-pip \
  nginx

RUN pip install https://github.com/graphite-project/ceres/tarball/master && \
  pip install whisper && \
  pip install carbon && \
  pip install graphite-web
  
# Configure Whisper, Carbon and Graphite-Web
ADD ./graphite/initial_data.json /opt/graphite/webapp/graphite/initial_data.json
ADD ./graphite/local_settings.py /opt/graphite/webapp/graphite/local_settings.py
ADD ./graphite/carbon.conf /opt/graphite/conf/carbon.conf
ADD ./graphite/storage-schemas.conf /opt/graphite/conf/storage-schemas.conf
ADD ./graphite/storage-aggregation.conf /opt/graphite/conf/storage-aggregation.conf

# configure nginx
RUN rm /etc/nginx/sites-enabled/default
ADD nginx/nginx.conf /etc/nginx/nginx.conf
ADD nginx/graphite.conf /etc/nginx/sites-available/graphite.conf
RUN ln -s /etc/nginx/sites-available/graphite.conf /etc/nginx/sites-enabled/graphite.conf

# daemons
ADD daemons/carbon.sh /etc/service/carbon/run
ADD daemons/carbon-aggregator.sh /etc/service/carbon-aggregator/run
ADD daemons/graphite.sh /etc/service/graphite/run
#ADD daemons/nginx.sh /etc/service/nginx/run

EXPOSE 80 2003
ENTRYPOINT ["/usr/sbin/nginx"]

