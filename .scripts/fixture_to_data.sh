#!/bin/bash

# download required jars
# source path
# dest path

if [ "$#" -ne 2 ]; then
    echo "Illegal number of parameters: [$0 source_file dest_file]"
    exit 1
    else:
    echo "[$0 $1 $2]"
fi

python -c 'import sys, yaml, json; json.dump(yaml.load(sys.stdin), sys.stdout, indent=2)' < $1 > $2