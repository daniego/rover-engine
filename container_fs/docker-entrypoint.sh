#!/bin/bash
mkdir /var/log/supervisor
supervisord -c /etc/supervisor/supervisord.conf -n
