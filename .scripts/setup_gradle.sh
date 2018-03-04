

#!/usr/bin/env bash

[ -z "${LIBS_PATH}" ] && echo "Env var 'LIBS_PATH' required"  && exit 1;
[ -z "${TEST_PATH}" ] && echo "Env var 'TEST_PATH' required"  && exit 1;
[ -z "${BUILD_PATH}" ] && echo "Env var 'BUILD_PATH' required"  && exit 1;
[ -z "${SOURCE_PATH}" ] && echo "Env var 'SOURCE_PATH' required"  && exit 1;
[ -z "${WORKSPACE_GRADLE}" ] && echo "Env var 'WORKSPACE_GRADLE' required"  && exit 1;
# cp = classpath @path of the build source

mkdir $WORKSPACE_GRADLE -p
cd $WORKSPACE_GRADLE

# start gradle if build.gradle does not exist
if [ ! -f build.gradle ]; then
    echo "File not found!"
    gradle init --type java-library
fi

# clean residual source_code
rm src -rf

./gradlew # prewarmup, pull dependencies

