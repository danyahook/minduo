#!/bin/bash

set -e

export LANG='en_US.UTF-8'

if [ "$1" = "serve" ] || [ "$1" = "" ]; then
    command="cd /usr/src/minduo/src && \
        python3 manage.py migrate && \
        python manage.py runserver 0.0.0.0:8000"
else
    command="exec sh"
fi

eval "${command}"
