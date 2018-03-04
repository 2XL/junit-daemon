#!/usr/bin/env bash


# download required jars
[ -z "${LIBS_PATH}" ] && echo "Env var 'LIBS_PATH' required"  && exit 1;
[ -z "${TEST_PATH}" ] && echo "Env var 'TEST_PATH' required"  && exit 1;
[ -z "${BUILD_PATH}" ] && echo "Env var 'BUILD_PATH' required"  && exit 1;




EXTERNAL_LIBS=$(find ${LIBS_PATH} -name *.jar)
EXTERNAL_LIBS=$(echo $EXTERNAL_LIBS | sed 's/ /:/g')

find ${TEST_PATH} -name '*Test.java' -exec javac -cp ${EXTERNAL_LIBS}:${BUILD_PATH} -d ${TEST_PATH} {} + 2>&1 "${REPORT_PATH}/out_compile_test.txt"