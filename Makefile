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

# ----------------------------------------------------------------------------------------
## setup, download jars, install dependencies, validate requirements
setup:
	@setup.sh


#-----------------------------------------------------------------------------------------
## yml fixtures into json requests --> from fixture/request.yml into data/data.json
fixture-2-json:
	@# list all fixtures
	@# for each fixture apply
	@fixture_to_data.sh ${FIXTURE_PATH}/request.yml ${DATA_PATH}/data.json


# ----------------------------------------------------------------------------------------
## build project tree from data/data.json
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

## clean
clean:
	@clean.sh

## logs
logs:
	@cat ${REPORT_PATH}/*

#-----------------------------------------------------------------------------------------

## all
all: build setup compile-source compile-test run-test logs




