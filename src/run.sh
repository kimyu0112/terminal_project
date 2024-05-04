#!/bin/bash

# Check whether correct version of Python is installed
if ! hash python; then
    echo "python is not installed"
    exit 1
fi

ver=$(python -V 2>&1 | sed 's/.* \([0-9]\).\([0-9]\).*/\1\2/')
if [ "$ver" -lt "27" ]; then
    echo "This script requires python 2.7 or greater"
    exit 1
fi

#Source code from: https://stackoverflow.com/questions/6141581/detect-python-version-in-shell-script

# Create virtual environment to separate package installations for different projects

Python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install packages from requirements.txt
pip3 install -r requirements.txt

# Run application
python3 main.py

# Deactivate virtual environment
deactivate