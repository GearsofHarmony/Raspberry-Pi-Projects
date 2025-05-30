#!/bin/bash

curl -fsSL https://download.docker.com/linux/debian/gpg | gpg -o /usr/share/keyrings/docker.gpg --dearmor
echo \
	"deb [ arch=$(uname -m) signed-by=/usr/share/keyrings/docker.gpg ] https://download.docker.com/linux/debian bookworm stable" | \
	tee /etc/apt/sources.list.d/docker.list
apt-get update

apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
docker run hello-world
