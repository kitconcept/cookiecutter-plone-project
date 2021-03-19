SHELL := /bin/bash
CURRENT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))


# We like colors
# From: https://coderwall.com/p/izxssa/colored-makefile-for-golang-projects
RED=`tput setaf 1`
GREEN=`tput setaf 2`
RESET=`tput sgr0`
YELLOW=`tput setaf 3`

.PHONY: all
all: build


# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
.PHONY: help
help: ## This help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: clean
clean: ## Clean
	rm -rf bin include lib .Python

.PHONY: build
build: ## Create virtualenv and install dependencies
	@echo "$(GREEN)==> Setup Virtual Env$(RESET)"
	python3 -m venv .
	bin/pip install pip --upgrade
	bin/pip install -r requirements.txt --upgrade

.PHONY: generate
generate: ## Create a sample package
	@echo "$(GREEN)==> Creating new test package$(RESET)"
	rm -rf projecttitle.projectname
	./bin/cookiecutter . --no-input

.PHONY: test
test: ## Create a sample package and tests it (runs buildout)
	@echo "$(GREEN)==> Creating new test package$(RESET)"
	rm -rf projecttitle.projectname
	./bin/cookiecutter . --no-input
	(cd projecttitle.projectname && virtualenv -p python3 --clear .)
	(cd projecttitle.projectname && bin/pip install pip --upgrade)
	(cd projecttitle.projectname && bin/pip install -r requirements.txt)
	(cd projecttitle.projectname && bin/buildout)
	(cd projecttitle.projectname && bin/test)
