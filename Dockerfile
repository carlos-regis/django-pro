# Pull base python image
FROM python:3.11.5-slim-bullseye

# Set environment variables
ENV \
    # Python
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # Pip
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_ROOT_USER_ACTION=ignore \
    # Poetry
    POETRY_VERSON=1.6.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local'

# Path
# ENV PATH='$POETRY_HOME/bin:$PATH'
# PYTHONPATH='$PYTHONPATH:.'

# Work directory
WORKDIR /app

# System dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install --no-install-recommends -y \
        # build-essential \
        curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    # Cleaning cache:
    apt-get purge --auto-remove -y -o APT::AutoRemove::RecommendsImportant=false && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

# Poetry dependencies
COPY ./poetry.lock ./pyproject.toml ./

# Install only the package dependencies here
RUN poetry config virtualenvs.create false && \
    poetry install --no-cache --no-interaction --no-root --no-ansi --with dev,test

# Copy project
COPY . .
