FROM     ubuntu:14.04.1

# Install prerequisites
RUN apt-get -y update && \
  
  # for graphite
  apt-get -y install python-dev \
  python-pip \
  libcairo2 \
  libffi-dev \
  
  nginx \
  
  # for grafana
  wget \
  adduser \
  libfontconfig

RUN pip install https://github.com/graphite-project/ceres/tarball/master \
  Django \
  django-tagging \
  Twisted \
  
  pytz \
  cairocffi \ 
  cffi \
  
  whisper \
  carbon \
  graphite-web \
  
  uwsgi

RUN wget https://grafanarel.s3.amazonaws.com/builds/grafana_2.0.2_amd64.deb && \
  dpkg -i grafana_2.0.2_amd64.deb && \
  rm grafana_2.0.2_amd64.deb
  
# Configure Whisper, Carbon and Graphite-Web
ADD ./graphite/initial_data.json /opt/graphite/webapp/graphite/initial_data.json
ADD ./graphite/local_settings.py /opt/graphite/webapp/graphite/local_settings.py
ADD ./graphite/carbon.conf /opt/graphite/conf/carbon.conf
ADD ./graphite/storage-schemas.conf /opt/graphite/conf/storage-schemas.conf
ADD ./graphite/storage-aggregation.conf /opt/graphite/conf/storage-aggregation.conf
ADD ./graphite/wsgi.py /opt/graphite/conf/wsgi.py
RUN python /opt/graphite/webapp/graphite/manage.py syncdb --noinput
RUN chown -R www-data:www-data /opt/graphite/webapp/ /opt/graphite/storage/

# TODO configure Grafana

# configure nginx
ADD nginx/nginx.conf /etc/nginx/nginx.conf
ADD nginx/graphite.conf /etc/nginx/sites-available/graphite.conf
RUN ln -s /etc/nginx/sites-available/graphite.conf /etc/nginx/sites-enabled/graphite.conf

# configure uwsgi
ADD uwsgi/graphite.ini /etc/uwsgi/graphite.ini

# TODO Add shared volumes 

EXPOSE 8080 2003 3000

CMD /opt/graphite/bin/carbon-cache.py start && \
  /usr/local/bin/uwsgi -d --ini /etc/uwsgi/graphite.ini && \
  service grafana-server start && \
  /etc/init.d/nginx start