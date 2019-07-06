#!/bin/bash

docker run --user $(id -u):$(id -g) -v $PWD/src/:/apps/ mario21ic/api-flask:latest flake8
