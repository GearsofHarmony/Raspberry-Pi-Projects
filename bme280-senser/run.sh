#!/bin/bash
ENV=$(pwd)/.env
PIP=${ENV}/bin/pip3
PYTHON=${ENV}/bin/python3
DIR=$(pwd)/src/

init_run() {
    echo "Checking existence of environment"
    if [ ! -d $ENV ]; then
        echo "Building Python Environment"
        python3 -m venv $ENV --system-site-packages
        $PIP -r req-packs.txt
    fi
    echo "Done!"
}


init_run

for file in ${DIR}bme280-test.py ${DIR}read_bme280_data.py
do
    echo "Running ${file}"
    $PYTHON $file
done