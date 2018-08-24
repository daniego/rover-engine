FROM resin/rpi-raspbian
MAINTAINER Daniel Floris <daniel.floris@gmail.com>

RUN apt-get update && \
    apt-get install -y \
    nginx \
    build-essential \
    python3 \
    python3-venv \
    python3-dev \
    python-pip && \
    rm -rf /var/lib/apt/lists/* && \
    pip install supervisor supervisor-stdout && \
    install -d /var/log/uwsgi -m=0777 && \
    echo "source /opt/rover-engine/bin/activate" >> /root/.bashrc

RUN mkdir /etc/supervisor && \
    echo_supervisord_conf > /etc/supervisor/supervisord.conf && \
    printf '[include]\nfiles = /etc/supervisor/conf.d/*.conf' >> /etc/supervisor/supervisord.conf && \
    rm /etc/nginx/sites-enabled/default

RUN python3 -m venv /opt/rover-engine

# I'm adding the requirements before the project files in order to reduce the build speed in case of code changes
ADD requirements.txt /srv/rover-engine/requirements.txt

RUN cd /srv/rover-engine/ && \
    /opt/rover-engine/bin/pip install -r requirements.txt


ADD container_fs /

ADD engine/ /srv/rover-engine/engine

WORKDIR /srv/rover-engine

EXPOSE 80 443 8099

ENTRYPOINT /docker-entrypoint.sh
