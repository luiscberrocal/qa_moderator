#!/usr/bin/env bash

docker container exec -it qa_moderator_django_1 pip list --outdated --format=columns

