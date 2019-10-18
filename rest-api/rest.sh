#!/bin/bash

set -e

pip3 install pymongo falcon gunicorn

gunicorn -b 0.0.0.0:8000 rest:app
