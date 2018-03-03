#!/usr/bin/env bash

# download required jars
[ -z "${LIBS_PATH}" ] && echo "Env var 'LIBS_PATH' required"  && exit 1;

awk -v LIBS_PATH=${LIBS_PATH} '{system("[ ! -f "LIBS_PATH"/"$1" ] && wget -O "LIBS_PATH"/"$1" "$2)}' libs/jar.repo.list

