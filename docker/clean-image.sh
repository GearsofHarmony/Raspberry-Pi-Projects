#!/bin/bash

docker container stop pi-test
docker container rm pi-test
docker image rm local:pi-test