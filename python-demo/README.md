This project demonstrates a Dockerized Python application using the `python:3.12-slim` base image.

The application prints:

- Current Python Version
- Current Date and Time

```bash
docker build -t python-datetime-app .
```

## Run Docker Container

```bash
docker run --rm python-datetime-app