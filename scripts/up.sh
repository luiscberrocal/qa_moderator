#!/usr/bin/env bash
docker stop $(docker ps -qa)
docker-compose -f local.yml up --build
