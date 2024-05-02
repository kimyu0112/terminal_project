#!/bin/bash

# python3 -m venv .venv
source .venv/bin/activate
pip3 install --disable-pip-version-check --quiet -r requirements.txt
python3 main.py