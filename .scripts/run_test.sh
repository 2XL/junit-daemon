#!/usr/bin/env bash

[ -z "${LIBS_PATH}" ] && echo "Env var 'LIBS_PATH' required"  && exit 1;
[ -z "${TEST_PATH}" ] && echo "Env var 'TEST_PATH' required"  && exit 1;
[ -z "${BUILD_PATH}" ] && echo "Env var 'BUILD_PATH' required"  && exit 1;
# cp = classpath @path of the build source


EXTERNAL_LIBS=$(find ${LIBS_PATH} -name *.jar)
EXTERNAL_LIBS=$(echo $EXTERNAL_LIBS | sed 's/ /:/g')


#TEST_CLASSES=$(find ${TEST_PATH} -name *.class)
#TEST_CLASSES=$(echo $TEST_CLASSES | sed 's/ /:/g')
#
#BUILD_CLASSES=$(find ${BUILD_PATH} -name *.class)
#BUILD_CLASSES=$(echo $BUILD_CLASSES | sed 's/ /:/g')

#echo ${BUILD_CLASSES}:${TEST_CLASSES}:${EXTERNAL_LIBS}

COLLECT_TESTS=$(command ls tests --hide='*.java' | sed -e 's/\..*$//' | awk '{print $NS}')

echo "java -cp ${BUILD_PATH}:${TEST_PATH}:${EXTERNAL_LIBS} org.junit.runner.JUnitCore $COLLECT_TESTS"
java -cp ${BUILD_PATH}:${TEST_PATH}:${EXTERNAL_LIBS} org.junit.runner.JUnitCore $COLLECT_TESTS > "${REPORT_PATH}/out_run_test.txt"


# java -cp .:/usr/share/java/junit.jar org.junit.runner.JUnitCore [test class name]
