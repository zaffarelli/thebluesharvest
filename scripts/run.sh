#!/usr/bin/env bash
PORT_USED="8086"

# Typical django stuff
python ./manage.py makemigrations
python ./manage.py migrate
python ./manage.py collectstatic --no-input

# Copy the images to the media root (and do some clean up)
mkdir -p /srv/thebluesharvest_media/{pictures,thumbnails,watermarked,raw}/
rm -rf /srv/thebluesharvest_media/{pictures,thumbnails,watermarked,raw}/*
cp ./frontdoor/media/pictures/*.jpg /srv/thebluesharvest_media/raw/
# Do the magic on the pictures
python ./manage.py shell < ./scripts/prepare_prod.py

# Launch the server
sudo fuser -k $PORT_USED/tcp
sudo lsof -t -i tcp:$PORT_USED | xargs kill -9
python ./manage.py runserver 0.0.0.0:$PORT_USED
