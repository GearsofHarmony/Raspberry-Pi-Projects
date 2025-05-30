#!/bin/bash

docker image build --tag local:pi-test .
docker container run -it --name pi-test local:pi-test