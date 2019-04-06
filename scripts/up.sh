#!/usr/bin/env bash
docker stop $(docker ps -qa)
docker-compose -f local.yml -f vuejs2.yml up
