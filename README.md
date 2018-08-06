# docker-pipenv-sample

This is a minimal example of using pipenv to install dependencies for a containerized Python project.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for fun.
If you want to use pipenv to manage your Python dependencies in your project that should run in Docker
you should start with inspecting the Dockerfile in this repository.


### Prerequisites

* **Docker**: If you still need to install this, you might want to check out [the Docker documentation](https://docs.docker.com/install/).


### Building from source 

1. Get a local copy of the repository and navigate to the project directory.

2. Inside the project directory, run the command below. This will build the image.
```bash
    docker build -t docker-pipenv-sample .
```

3. Run a container based on the image.
```bash
    docker run -p 5000:5000 docker-pipenv-sample
```

4. Use [Pipenv](https://github.com/pypa/pipenv) to manage your Python dependencies from now on with it. Please.

5. Read the Dockerfile and see how easy it is to adapt it for your project.

### Building from Container Registry

You can also get a pre-built image from the [Gitlab Container Registry](https://gitlab.com/dfederschmidt/docker-pipenv-sample/container_registry). But where is the fun in that?

```bash
docker run -p 5000:5000 registry.gitlab.com/dfederschmidt/docker-pipenv-sample:latest
```

## Running tests

To run the test locally use the command below.

```bash
pipenv install
python tests.py 
```

It also runs on every new change as part of a [Gitlab CI/CD pipeline](https://gitlab.com/dfederschmidt/docker-pipenv-sample/pipelines).

## Built With

* [Docker](https://www.docker.com/what-docker)
* [Pipenv](https://docs.pipenv.org/)
* [Flask](http://flask.pocoo.org/)

## Contributing

Feel free to open [issues](https://gitlab.com/dfederschmidt/docker-pipenv-sample/issues) / [pull requests](https://gitlab.com/dfederschmidt/docker-pipenv-sample/merge_requests) on [Gitlab](https://gitlab.com/dfederschmidt/docker-pipenv-sample).

## Versioning

[Changelog](https://gitlab.com/dfederschmidt/docker-pipenv-sample/blob/master/CHANGELOG) can be found on Gitlab.

[SemVer](https://semver.org/). See [repository tags](https://gitlab.com/dfederschmidt/docker-pipenv-sample).


## Authors

* **Daniel Federschmidt** - *all the things* - [federschmidt.xyz](https://federschmidt.xyz)

## Acknowledgments

* [Kenneth Reitz](https://www.kennethreitz.org/) for conceiving Pipenv - awesome tool :cake:.
