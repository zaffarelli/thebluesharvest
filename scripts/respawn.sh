#!/usr/bin/env bash

cd ~/thebluesharvest

sudo chown -R www-data:www-data /srv
sudo chmod -R a+w /srv


cd ./frontdoor/media/
cp -R * /srv/thebluesharvest_media/
cd ../..

pip install -r requirements_demo.txt

python ./manage.py migrate
python ./manage.py collectstatic --no-input

python ./manage.py shell < ./scripts/prepare_prod.py

./scripts/super.sh restart thebluesharvest
