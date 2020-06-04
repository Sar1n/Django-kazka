.PHONY: build							#build containers
build:
	docker-compose --build

.PHONY: up								#start container
up:
	docker-compose up

.PHONY: run								#build & start container
run:
	docker-compose up --build

.PHONY: clean							#remove all container images and docker additionals (networks etc.)
clean:
	docker system prune -f
	docker image prune -af

.PHONY: down							#stop container
down:
	docker-compose down