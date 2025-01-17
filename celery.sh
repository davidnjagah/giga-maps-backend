#!/usr/bin/env bash
set -ex

# export environment variables to make them available in ssh session
for var in $(compgen -e); do
    echo "export $var=${!var}" >> /etc/profile
done

echo "Starting SSH ..."
service ssh start

export FLASK_APP=hello.py
pipenv run python -m flask run --host 0.0.0.0 --port 8000 &

# pipenv run celery -A proco.taskapp worker $*
# --logfile=/code/celeryd-%n.log --loglevel=DEBUG

if $ENABLED_FLOWER_METRICS; then
    echo "Starting worker ..."
    pipenv run celery --app=proco.taskapp worker --concurrency=3 --time-limit=300 --soft-time-limit=60 $* &

    echo "Starting flower ..."
    pipenv run celery --app=proco.taskapp flower
else
    echo "Starting worker ..."
    pipenv run celery --app=proco.taskapp worker --concurrency=3 --time-limit=300 --soft-time-limit=60 $*
fi
