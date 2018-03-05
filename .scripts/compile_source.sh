#!/bin/bash

# download required jars
[ -z "${SOURCE_PATH}" ] && echo "Env var 'SOURCE_PATH' required"  && exit 1;
[ -z "${BUILD_PATH}" ] && echo "Env var 'BUILD_PATH' required"  && exit 1;
[ -z "${REPORT_PATH}" ] && echo "Env var 'REPORTS_PATH' required"  && exit 1;

[ ! -d "${REPORT_PATH}" ] && mkdir ${REPORT_PATH}
[ ! -d "${BUILD_PATH}" ] && mkdir ${BUILD_PATH}
[ ! -d "${SOURCE_PATH}" ] && mkdir ${SOURCE_PATH}

# \; compile one by one
# +  compile with all found
find ${SOURCE_PATH} -name '*.java' -exec javac -d ${BUILD_PATH} {} + \
    2> "${REPORT_PATH}/err_compile_source.txt" \
    1> "${REPORT_PATH}/out_compile_source.txt"
