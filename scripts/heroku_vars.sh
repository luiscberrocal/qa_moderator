#!/usr/bin/env bash
heroku config:set DJANGO_AWS_ACCESS_KEY_ID=InvalidaKeyAWSNotCreated

heroku config:set DJANGO_AWS_SECRET_ACCESS_KEY=FalseAccesKeyJustT0Run

heroku config:set DJANGO_AWS_STORAGE_BUCKET_NAME=qa-moderator

heroku config:set CELERY_BROKER_URL=$REDIS_URL

heroku config:set DJANGO_ADMIN_URL=ist/

heroku config:set DJANGO_SECRET_KEY=N0S3ncan7losR3tosS13Mpr3SiSePuede_+uytttt

heroku config:set DJANGO_SETTINGS_MODULE=config.settings.production

heroku config:set USE_DOCKER=no

heroku config:set DJANGO_DEBUG=True







