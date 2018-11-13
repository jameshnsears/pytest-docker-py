#!/usr/bin/env bash

export VENV=venv-pytest-docker-py
source $VENV/bin/activate
export PYTHONPATH=src:$PYTHONPATH
pip install .
pytest -s --cov-report term-missing --cov . test/integration
deactivate
