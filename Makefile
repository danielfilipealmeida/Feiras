#constants
CONT_WEB=site
SITE_PATH=/home/root/feiras

# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
# A category can be added with @category
HELP_FUN = \
	%help; \
	while(<>) { push @{$$help{$$2 // 'options'}}, [$$1, $$3] if /^([a-zA-Z\-]+)\s*:.*\#\#(?:@([a-zA-Z\-]+))?\s(.*)$$/ }; \
	print "usage: make [target]\n\n"; \
	for (sort keys %help) { \
	print "${WHITE}$$_:${RESET}\n"; \
	for (@{$$help{$$_}}) { \
	$$sep = " " x (32 - length $$_->[0]); \
	print "  ${YELLOW}$$_->[0]${RESET}$$sep${GREEN}$$_->[1]${RESET}\n"; \
	}; \
	print "\n"; }

# Process parameters/options
ifeq (cli,$(firstword $(MAKECMDGOALS)))
    ifndef container
        CONTAINER := cli
        CUSTOM_SHELL := zsh
    else
        ifeq ($(filter $(container),$(CONTAINERS)),)
            $(error Invalid container. $(CONTAINER) does not exist in $(CONTAINERS))
        endif
        CONTAINER := $(container)
        CUSTOM_SHELL := /bin/sh
    endif

    ifdef shell
        CUSTOM_SHELL := $(shell)
    endif
#    RUN_ARGS := $(DOCKER_TAG)_$(CONTAINER)_1
endif

ifeq (composer-update,$(firstword $(MAKECMDGOALS)))
    PACKAGES =
    ifdef packages
        PACKAGES := $(packages)
    endif
endif

ifeq (logs,$(firstword $(MAKECMDGOALS)))
    LOGS_TAIL := 0
    ifdef tail
        LOGS_TAIL := $(tail)
    endif
endif

TEST_GROUP := -g Acceptance

ifeq (acceptance-tests,$(firstword $(MAKECMDGOALS)))
    ifdef group
        TEST_GROUP := -g $(group)
    endif
endif

help: ##@other Show this help.
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)
.PHONY: help

open: ##@other Opens all containers in browser tabs.
	open http://localhost:8881
.PHONY: open

console: ##@servers Run console inside the web container
	docker-compose exec $(CONT_WEB) $(SITE_PATH) $(COM)
.PHONY: console

manage: ##@servers Run manage.py inside the web container
	docker-compose exec $(CONT_WEB) python $(SITE_PATH)/manage.py $(COM)
.PHONY: console

load-all-fixtures: ##@dev Load all fixtures 
	make manage COM="loaddata locais"
	make manage COM="loaddata feiras"
.PHONY: load-all-fixtures

make-migrations: ##@dev Check for changes in the models and make new migrations if needed 
	make manage COM="makemigrations"
.PHONY: make-migrations

migrate: ##@dev Check for changes in the models and make new migrations if needed 
	make manage COM="migrate"
.PHONY: migrate