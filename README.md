# PyTube

Example project from ["Bootstrapping Microservices with Docker, Kubernetes, and Terraform"](https://www.manning.com/books/bootstrapping-microservices-with-docker-kubernetes-and-terraform) book.

Based on Python + Flask.

## Microservices

At this moment (incomplete) project consists of 3 microservices and database:

1. Video streaming service. Gets video id from query param, retrives video info from *metadata* service and pass video stream from *video storage* service to client.
2. Video storage service. Uses Azure Blob storage for videos storage and returns stream by path for *video streaming* service.
3. History service. Receives "viewed" events from *video streaming* service by *RabbitMQ* puts it into *database*.
4. MongoDB for storing data.
5. RabbitMQ for indirect communications.
6. Recommendations service. Receives "viewed" events by *RabbitMQ* and simply prints it to console.
7. Metadata service. Provides video metadata to other services.

## Requirements

* docker
* docker-compose

### Optional

* make

## How to start?

Use `make up` and `make down` to start and stop containers.

Use `make dev` for development with support of live reload by `watchgod`.

## See also

* Go + Fiber version: https://github.com/capcom6/go-tube
* NodeJS + Express version: https://github.com/capcom6/node-tube
