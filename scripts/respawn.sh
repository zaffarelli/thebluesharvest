#!/usr/bin/env bash

cd ~/thebluesharvest

sudo chown -R www-data:www-data /srv
sudo chmod -R a+w /srv

pip install -r requirements.txt

python ./manage.py migrate
python ./manage.py collectstatic --no-input
./scripts/super.sh restart thebluesharvest
