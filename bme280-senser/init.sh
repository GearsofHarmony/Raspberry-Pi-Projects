#!/bin/bash

python3 -m venv $(pwd)/.env --system-site-packages
$(pwd)/.env/bin/pip3 install -r req-packs.txt