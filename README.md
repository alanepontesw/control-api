[![Build Status](https://travis-ci.org/alanepontesw/control-api.svg?branch=master)](https://travis-ci.org/alanepontesw/control-api)

# Project Title

Manager API Request

## Base structure

### Folders 
requirements/
src/
- domain/
- config/
- interface/
- infrastructure/ 
  
### Using Scripts to Gitflow

Make sure you have permissions for all files
```
$ chmod +x ./feature.sh (...)
```

```
To create a new feature-branch:
$ ./feature.sh "feature-name"

To commit in the current branch:
$ ./commit.sh "commit-message"

To make a hot fix (branch master only):
$ ./hotfix "hotfix-name"

To push in the current branch:
$ ./push

To synchronize the flow of new commits in order to avoid possible conflicts:
$ ./sincflow
```

### CI/CD
Using Travis, for now, just have continuos integration

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites    

Be sure, have installed:
- Python3.5
- Pip
- Redis

You will need to install in your machine the following packages: 
- redis
- flask-restful
- pylint
- pytest
- pycodestyle
- coverage

Installation via pip:

```
$ pip install -r requirements/develop.txt
```

If you'd like up and running using Docker, please, be sure you have:
- Docker
- Docker Compose 

Up and Running via Docker Compose:

```
$ docker-compose up
```

### Envs
    PYTHONPATH - It's the path to source app (src/)
    REDIS_DATABASE - It's the database created on Redis
    REDIS_HOST - It's the host running redis-server
    REDIS_PASSWORD - It's password to connect to Redis, if you have one.
    REDIS_PORT - Specifies the port for the connection.

### Installing

A step by step series of examples that tell you how to get a development env running

Be sure you have exported all env vars

```
$ pip install -r requirements/develop.txt
$ python src/core.py
```

Or, you can easily use Docker Compose

```
$ docker-compose up
```

## Running the tests

To execute the tests, run:

```
$ pytest src/tests
```

Be sure, have installed all libraries using:

```
$ pip install -r requirements/develop.txt
```

It's also necessary to export the environment variables described above.

## Running the lint

To run lint for your code, execute:

```
$ pylint src/ tests/
```

## Deployment
TODO

