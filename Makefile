COMPOSE = docker-compose

help:
	@echo ""
	@echo "The following commands are available:"
	@echo ""
	@echo " \x1b[35mGeneric commands:\x1b[0m"
	@echo "   \x1b[32mmake init\x1b[0m          Initialize local dev environment (login to gcloud)."
	@echo "   \x1b[32mmake build\x1b[0m         Build all docker images required to run the project."
	@echo "   \x1b[32mmake start\x1b[0m         Start the app (backend & frontend)"
	@echo "   \x1b[32mmake checks\x1b[0m        Run all code checks (backend & frontend)"
	@echo "   \x1b[32mmake deploy\x1b[0m        Run all code checks (backend & frontend)"
	@echo ""
	@echo " \x1b[35mAPI backend commands:\x1b[0m"
	@echo "   \x1b[32mmake api\x1b[0m           Start the API backend only"
	@echo "   \x1b[32mmake api-shell\x1b[0m     Run code checks against the API backend"
	@echo "   \x1b[32mmake api-checks\x1b[0m    Run code checks against the API backend"
	@echo "   \x1b[32mmake api-lint\x1b[0m      Run code checks against the API backend"
	@echo "   \x1b[32mmake api-test\x1b[0m      Run code checks against the API backend"
	@echo ""
	@echo " \x1b[35mFrontend commands:\x1b[0m"
	@echo "   \x1b[32mmake fe-dev\x1b[0m        Run code checks against the API backend"
	@echo "   \x1b[32mmake fe-checks\x1b[0m     Run code checks against the API backend"
	@echo ""

init:
	$(COMPOSE) run api gcloud auth login

build:
	$(COMPOSE) build

start:
	$(COMPOSE) up

checks: api-checks fe-checks

deploy: checks
	@echo "Deploying"

clean:
	@echo "\x1b[35m--- Removing temporary files ---\x1b[0m"
	@$(COMPOSE) run api peltak clean

api:
	$(COMPOSE) up api

api-shell:
	$(COMPOSE) run --rm api /bin/sh

api-test: clean
	@$(COMPOSE) run api peltak lint

api-lint:
	@$(COMPOSE) run api peltak test

api-checks: api-test api-lint

fe-checks:
	@echo "\x1b[35m--- Running frontend checks ---\x1b[0m"
