FROM python:3.12-slim

WORKDIR /app
COPY /mlops/modeling .
COPY poetry.lock .
COPY pyproject.toml .

ENV POETRY_VERSION=1.5.1
ENV PATH="/root/.local/bin:$PATH"

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl git python3-pip && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN poetry config virtualenvs.create false && poetry install
