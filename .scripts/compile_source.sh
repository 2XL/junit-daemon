#!/bin/bash

# download required jars
[ -z "${SOURCE_PATH}" ] && echo "Env var 'SOURCE_PATH' required"  && exit 1;
[ -z "${BUILD_PATH}" ] && echo "Env var 'BUILD_PATH' required"  && exit 1;
[ -z "${REPORT_PATH}" ] && echo "Env var 'REPORTS_PATH' required"  && exit 1;


# \; compile one by one
# +  compile with all found
find ${SOURCE_PATH} -name '*.java' -exec javac -d ${BUILD_PATH} {} + > "${REPORT_PATH}/out_compile_source.txt"
