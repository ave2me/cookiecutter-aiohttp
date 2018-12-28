FROM python:3.7.1-alpine

RUN mkdir -p /opt/project/auth
RUN pip --no-cache-dir install poetry

COPY ./pyproject.toml /opt/project
COPY poetry.lock /opt/project

RUN cd /opt/project && poetry install --no-dev

WORKDIR /opt/project

ENTRYPOINT poetry run python -m aiohttp.web {{cookiecutter.project_name}}.main:main