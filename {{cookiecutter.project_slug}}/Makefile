SHELL := /bin/bash
CURRENT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))


# We like colors
# From: https://coderwall.com/p/izxssa/colored-makefile-for-golang-projects
RED=`tput setaf 1`
GREEN=`tput setaf 2`
RESET=`tput sgr0`
YELLOW=`tput setaf 3`

.PHONY: all
all: build code-analysis test test-acceptance

# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
.PHONY: help
help: ## This help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: test
build-frontend:  ## Build React Frontend
	@echo "Build Frontend"
	yarn
	yarn build

.PHONY: build-backend
build-backend: build

bin/python bin/pip::
	@echo "$(GREEN)==> Setup Virtual Env$(RESET)"
	(cd api && virtualenv -p python3 --clear .)

.PHONY: build
build: bin/pip ## Create virtualenv and run buildout
	@echo "$(GREEN)==> Setup Build$(RESET)"
	(cd api && bin/pip install pip --upgrade)
	(cd api && bin/pip install -r requirements.txt --upgrade)
	(cd api && bin/buildout)

.PHONY: build-backend-dev
build-backend-dev: ## Create virtualenv and run dev buildout
	@echo "$(GREEN)==> Setup Build$(RESET)"
	(cd api && bin/pip install pip --upgrade)
	(cd api && bin/pip install -r requirements.txt --upgrade)
	(cd api && bin/buildout -c dev.cfg)

.PHONY: build-backend-staging
build-backend-staging: ## Create virtualenv and run staging buildout
	@echo "$(GREEN)==> Setup Build$(RESET)"
	(cd api && bin/pip install pip --upgrade)
	(cd api && bin/pip install -r requirements.txt --upgrade)
	(cd api && bin/buildout -c staging.cfg)

.PHONY: build-backend-live
build-backend-live: ## Create virtualenv and run live buildout
	@echo "$(GREEN)==> Setup Build$(RESET)"
	(cd api && bin/pip install pip --upgrade)
	(cd api && bin/pip install -r requirements.txt --upgrade)
	(cd api && bin/buildout -c live.cfg)

.PHONY: clean
clean: ## Remove old virtualenv and creates a new one
	@echo "$(RED)==> Cleaning environment and build$(RESET)"
	(cd api && rm -rf bin lib include share develop-eggs .Python parts .installed.cfg .mr.developer.cfg)

.PHONY: code-analysis
code-analysis: ## Run static code analysis
	@echo "$(GREEN)==> Run static code analysis$(RESET)"
	(cd api && bin/code-analysis)

.PHONY: test
test:
	make test-backend
	make test-frontend

.PHONY: test-frontend
test-frontend:
	@echo "$(GREEN)==> Run Frontend Tests$(RESET)"
	yarn test

.PHONY: test-backend
test-backend: build ## Run tests
	@echo "$(GREEN)==> Run Backend Tests$(RESET)"
	(cd api && bin/test --xml)

.PHONY: test-acceptance
test-acceptance: ## Run acceptance tests
	@echo "$(GREEN)==> Run Acceptance Tests$(RESET)"
	bin/test-acceptance

.PHONY: start-backend
start-backend: ## Start Plone Backend
	@echo "$(GREEN)==> Start Plone Backend$(RESET)"
	(cd api && bin/instance fg)
