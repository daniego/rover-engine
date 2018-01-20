FROM resin/rpi-raspbian
MAINTAINER Daniel Floris <daniel.floris@gmail.com>

RUN apt-get update && \
    apt-get install -y \
    nginx \
    build-essential \
    python3 \
    python3-venv

ADD requirements.txt /srv/rover-engine/requirements.txt
RUN apt-get install -y python3-dev
RUN python3 -m venv /opt/rover-engine
 # && \
RUN cd /srv/rover-engine/ && \
    /opt/rover-engine/bin/pip install -r requirements.txt

RUN echo "source /opt/rover-engine/bin/activate" >> /root/.bashrc


ADD etc/nginx/sites-enabled/nginx80 /etc/nginx/sites-enabled/nginx80
RUN rm /etc/nginx/sites-enabled/default
ADD etc/supervisor/conf.d/engine.conf /etc/supervisor/conf.d/engine.conf

ADD engine/ /srv/rover-engine/engine

WORKDIR /srv/rover-engine

EXPOSE 80 8099

ENTRYPOINT /opt/rover-engine/bin/python /srv/rover-engine/engine/main.py
