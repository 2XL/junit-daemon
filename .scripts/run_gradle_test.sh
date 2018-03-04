#!/usr/bin/env bash

[ -z "${LIBS_PATH}" ] && echo "Env var 'LIBS_PATH' required"  && exit 1;
[ -z "${TEST_PATH}" ] && echo "Env var 'TEST_PATH' required"  && exit 1;
[ -z "${BUILD_PATH}" ] && echo "Env var 'BUILD_PATH' required"  && exit 1;
[ -z "${SOURCE_PATH}" ] && echo "Env var 'SOURCE_PATH' required"  && exit 1;
[ -z "${WORKSPACE_GRADLE}" ] && echo "Env var 'WORKSPACE_GRADLE' required"  && exit 1;
# cp = classpath @path of the build source


# clean residual source_code
rm $WORKSPACE_GRADLE/src -rf

# create directories
mkdir $WORKSPACE_GRADLE/src/main/java -p
mkdir $WORKSPACE_GRADLE/src/test/java -p

# mv fixture code to dirs
#find src -name *.java -exec cp {} $WORKSPACE_GRADLE/src/main/java \;
#find tests -name *.java -exec cp {} $WORKSPACE_GRADLE/src/test/java \;
# use rsync instead of cp, for directory prefix (include extension in subdirs) # use `--prune-empty-dirs` flag to skip empty dirs
echo "rsync"
rsync -av --include='*.java' --include='*/' --exclude='*' src $WORKSPACE_GRADLE/src/main/java
rsync -av --include='*.java' --include='*/' --exclude='*' tests $WORKSPACE_GRADLE/src/test/java


cd $WORKSPACE_GRADLE && ./gradlew test


