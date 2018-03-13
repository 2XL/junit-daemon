#!/usr/bin/env bash

# remove all pycache and pyc files before building docker image

find . | grep -E "(__pycache__|\.pyc$)" | xargs rm -rf
find . -name "*.pyc" -exec rm -f {} \;
