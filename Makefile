DOCKER_COMPOSE = docker-compose
DOCKER_COMPOSE_FILE = docker-compose.yml
CONTAINER_NAME = backend

.PHONY: all build up down clean restart logs test

all: help

##help        | Show this text
help: Makefile
	@sed -n 's/^##//p' $< | cat

##build       | Build the application
build:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) up --build --force-recreate --remove-orphans

##up          | Build and start the application
up:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) up -d

##down        | Stop the application
down:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) down

##ps          | Lists containers
ps:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) ps

##clean       | Down and Remove images
clean:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) down -v --rmi all --remove-orphans

##restart     | Restart the application
restart: down up

##logs        | Show logs of the application
logs:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) logs -f

##upgrade     | Run DB upgrade
upgrade:
	if [ -z $(id) ]; then \
         $(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE)  run --rm $(CONTAINER_NAME) poetry run alembic upgrade head; \
      else \
       $(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE)  run --rm $(CONTAINER_NAME) poetry run alembic upgrade $(id); \
    fi

##downgrade   | Run DB downgrade
downgrade:
	if [ -z $(id) ]; then \
        $(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) run --rm $(CONTAINER_NAME) poetry run alembic downgrade base; \
    else \
        $(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) run --rm $(CONTAINER_NAME) poetry run alembic downgrade $(id); \
    fi

##migrate     | Run DB revision. Set 'msg' arg.
revision:
	if [ -z $(msg) ]; then \
       echo "Especifique un mensaje para la migracion."; \
        return 1; \
    else \
        $(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) run --rm $(CONTAINER_NAME) poetry run alembic revision --autogenerate -m $(msg); \
    fi

##lint        | Run lint commands to check types, import and formats
lint:
	$(DOCKER_COMPOSE) -f $(DOCKER_COMPOSE_FILE) run --rm $(CONTAINER_NAME) sh ./lint.sh
