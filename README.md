# devops a day at the office

A simple Python app, which makes requests to https://catfact.ninja/fact and prints the results to the terminal.

The application is packaged as a Docker image, which allows running it without installing anything but Docker.

## Requirements
[git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker](https://docs.docker.com/get-docker/) - that's it

## Usage
1. Git clone this repository
1. Build the image locally, tagging it as `1.0`
    ```
    docker build -t catfacts:1.0 .
    ```
1. Run an instance of the image (container), each invocation will print a random fact about cats
    ```
    docker run --rm  catfacts:1.0
    ```
    __NOTE__: the `--rm` flag tells Docker to remove the container when it's finished, since we don't need to keep any important data, we just print and quit, reference - [cleanup](https://docs.docker.com/engine/reference/run/#clean-up---rm)
