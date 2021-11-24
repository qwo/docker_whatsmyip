#/bin/sh

poetry run gunicorn main:app --bind :$PORT  --reload