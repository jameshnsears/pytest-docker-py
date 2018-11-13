#!/usr/bin/env bash

export VENV=venv-pytest-docker-py
source $VENV/bin/activate
export PYTHONPATH=src:$PYTHONPATH
pytest -s --cov-report term-missing --cov . test/unit
deactivate
