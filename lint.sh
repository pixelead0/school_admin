#!/usr/bin/env bash

set -x

poetry run mypy app --exclude=alembic
poetry run black app --exclude=alembic
poetry run isort app --skip=alembic
#poetry run flake8 --exclude=alembic --max-line-length=88 --exclude=.git,__pycache__,__init__.py,.mypy_cache,.pytest_cache
