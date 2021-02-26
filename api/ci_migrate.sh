#!/bin/bash

#docker-compose up -d
#docker-compose exec -u $(id -u):$(id -g) api /apps/migrate.sh
#docker-compose down

docker run --user "$(id -u):$(id -g)" -v $PWD/src/:/apps/ mario21ic/api-flask:latest /apps/migrate.sh
