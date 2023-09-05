#!/usr/bin/env bash

cd ./frontdoor/media/
cp -R * /srv/thebluesharvest_media/
cd ../..

python ./manage.py makemigrations
python ./manage.py migrate
python ./manage.py collectstatic --no-input


python ./manage.py shell < ./scripts/prepare_prod.py

python ./manage.py runserver 0.0.0.0:8086
