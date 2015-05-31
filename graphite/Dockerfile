FROM     ubuntu:14.04.1

# Install prerequisites
RUN apt-get -y update && \
  apt-get -y \
  install python-dev \
  python-pip \
  
  nginx \
  uwsgi-plugin-python \
  uwsgi

RUN pip install https://github.com/graphite-project/ceres/tarball/master && \
  pip install Django && \
  pip install django-tagging && \
  pip install whisper && \
  pip install carbon && \
  pip install graphite-web
  
# Configure Whisper, Carbon and Graphite-Web
ADD ./graphite/initial_data.json /opt/graphite/webapp/graphite/initial_data.json
ADD ./graphite/local_settings.py /opt/graphite/webapp/graphite/local_settings.py
ADD ./graphite/carbon.conf /opt/graphite/conf/carbon.conf
ADD ./graphite/storage-schemas.conf /opt/graphite/conf/storage-schemas.conf
ADD ./graphite/storage-aggregation.conf /opt/graphite/conf/storage-aggregation.conf
ADD ./graphite/wsgi.py /opt/graphite/conf/wsgi.py
RUN python /opt/graphite/webapp/graphite/manage.py syncdb --noinput
RUN chown -R www-data:www-data /opt/graphite/webapp/ /opt/graphite/storage/

# configure nginx
ADD nginx/nginx.conf /etc/nginx/nginx.conf
ADD nginx/graphite.conf /etc/nginx/sites-available/graphite.conf
RUN ln -s /etc/nginx/sites-available/graphite.conf /etc/nginx/sites-enabled/graphite.conf

# configure uwsgi
ADD uwsgi/graphite.ini /etc/uwsgi/apps-available/graphite.ini
RUN ln -s /etc/uwsgi/apps-available/graphite.ini /etc/uwsgi/apps-enabled/

EXPOSE 8080 2003
CMD /opt/graphite/bin/carbon-cache.py start && \
  /etc/init.d/uwsgi restart && \
  /etc/init.d/nginx restart && \
  /bin/bash