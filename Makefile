# fugoki-emulator-daemon Makefile
# Useful tooling for complex commands
# Specs: http://www.gnu.org/software/make/manual/make.html

# Env vars
export PATH := .scripts:$(PATH)
export LIBS_PATH := libs
export TEST_PATH := tests
export BUILD_PATH := out
export SOURCE_PATH := src
export REPORT_PATH := reports
export FIXTURE_PATH := fixture
export DATA_PATH := data

export WORKSPACE_GRADLE := ./workspace/gradle
export WORKSPACE_MAVEN := ./workspace/maven
export WORKSPACE_ANT := ./workspace/ant

export DOCKER_IMAGE_NAME := chenglongzq/junit-daemon

# COLORS
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
RESET  := $(shell tput -Txterm sgr0)


TARGET_MAX_CHAR_NUM=25

# ----------------------------------------------------------------------------------------

## Show help
help:
	@echo ''
	@echo 'Usage:'
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)


#
## DockerCompose && Docker tasks
dc-build:
	@docker-compose build


## get docker images size
dc-size:
	@docker images | grep "${DOCKER_IMAGE_NAME}"

dc-up:
	@docker-compose up

## get docker runner tty terminal
dc-bash: dc-build dc-size
	@docker run -it --rm "${DOCKER_IMAGE_NAME}" bash

# ----------------------------------------------------------------------------------------
## setup, download jars, install dependencies, validate requirements
setup:
	@setup.sh


setup-gradle:
	@setup_gradle.sh

#-----------------------------------------------------------------------------------------
## yml fixtures into json requests --> from fixture/exported_challenge.yml into data/exported_challenge.json
fixture-2-json:
	@# list all fixtures
	@# for each fixture apply
	@fixture_to_data.sh ${FIXTURE_PATH}/exported_challenge.yml ${DATA_PATH}/exported_challenge.json

## export project files into yml fixture
project-2-fixture:
	@invoke export

## project into fixture then fixture into json
project-2-fixture-json: project-2-fixture fixture-2-json

# ----------------------------------------------------------------------------------------
## build project tree from data/exported_challenge.json
build-project:
	@invoke -l
	@invoke build

## build project
build: build-project

# ----------------------------------------------------------------------------------------
## compile source class
compile-source:
	@compile_source.sh


## compile test
compile-test:
	@compile_test.sh


#-----------------------------------------------------------------------------------------
## run test
run-test:
	@run_test.sh

## run test with recompilation
run-test-recompile: compile-source compile-test run-test logs

## run gradle test
run-gradle:
	@run_gradle_test.sh

## clean
clean:
	@clean.sh
	@invoke clean

## stream logs
logs-stream:
	@tail reports/* -f

## logs
logs:
	@cat ${REPORT_PATH}/*

#-----------------------------------------------------------------------------------------

## all
all: build setup compile-source compile-test run-test logs


## all-gradle
all-gradle: build setup-gradle run-gradle


