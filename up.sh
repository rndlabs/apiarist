#!/bin/sh

# Make sure submodules etc are updated.
git submodule update --init --recursive

VENV=$(which virtualenv)

# First make sure a python virtual environment is installed
$VENV .virtualenv
source ./.virtualenv/bin/activate

# Install the requirements
pip install -r requirements.txt

# Now, generate all the files
python build.py

# Deploy to docker-compose
sh deploy.sh

# Install monBee dependencies
cd monBee
npm i