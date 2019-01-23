FROM python:3.7.1-alpine

RUN mkdir -p /opt/project/{{cookiecutter.proect_name}}
RUN pip --no-cache-dir install poetry

COPY ./pyproject.toml /opt/project
COPY poetry.lock /opt/project

RUN cd /opt/project && poetry install --no-dev

COPY ./{{cookiecutter.proect_name}} /opt/project/{{cookiecutter.proect_name}}
COPY ./{{cookiecutter.proect_name}}.yml /opt/project/{{cookiecutter.proect_name}}.yml

WORKDIR /opt/project

ENTRYPOINT poetry run python -m aiohttp.web {{cookiecutter.project_name}}.main:main