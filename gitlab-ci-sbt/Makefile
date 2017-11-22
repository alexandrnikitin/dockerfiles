NS = docker.company.com
REPO = product/project-build
VERSION ?= v0.1.0

NAME = image-name
INSTANCE = default

.PHONY: build push shell run start stop rm tag_latest release

build:
	docker build -t $(NS)/$(REPO):$(VERSION) .

push:
	docker push $(NS)/$(REPO):$(VERSION)
	docker push $(NS)/$(REPO):latest

shell:
	docker run --rm --name $(NAME)-$(INSTANCE) -i -t $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION) /bin/bash

run:
	docker run --rm --name $(NAME)-$(INSTANCE) $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION) $(CMD)

start:
	docker run -d --name $(NAME)-$(INSTANCE) $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION)

stop:
	docker stop $(NAME)-$(INSTANCE)

rm:
	docker rm $(NAME)-$(INSTANCE)

tag_latest:
	docker tag $(NS)/$(REPO):$(VERSION) $(NS)/$(REPO):latest

release: build tag_latest
	make push -e VERSION=$(VERSION)
