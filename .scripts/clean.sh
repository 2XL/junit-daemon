#!/usr/bin/env bash

[ -z "${TEST_PATH}" ] && echo "Env var 'TEST_PATH' required"  && exit 1;
[ -z "${BUILD_PATH}" ] && echo "Env var 'BUILD_PATH' required"  && exit 1;
[ -z "${REPORT_PATH}" ] && echo "Env var 'REPORT_PATH' required"  && exit 1;

find . -type f -name '*.jar' -delete
find . -type f -name '*.class' -delete

rm ${TEST_PATH}/*.class -rf -v
rm ${BUILD_PATH}/*.class -rf -v
rm ${REPORT_PATH}/* -rf -v
rm state -rf -v