CONTAINER_NAME = peanut-app
PUBLISH_PORT = 8000:80

all: setup clean build run
		@echo "done"

.PHONY: clean
clean:
		@if [[ -f .container-id ]]; \
		then \
			echo "stopping docker container"; \
			cat .container-id | xargs docker stop; \
			rm .container-id; \
		fi;
		@docker ps -a -q | xargs docker rm
		@echo "removing old docker images"
		@docker images --no-trunc | grep 'none' | awk '{print $3}' | xargs docker rmi


.PHONY: build
build: clean
		@echo "building docker container"
		@docker build -t $(CONTAINER_NAME) .


.PHONY: run
run: build
		@echo "starting docker container"
		@CONTAINER_ID="$(shell docker run -p $(PUBLISH_PORT) -d $(CONTAINER_NAME))"; \
		echo $$CONTAINER_ID >> .container-id;

.PHONY: vagrant
vagrant:
		@vagrant up --provider=docker
