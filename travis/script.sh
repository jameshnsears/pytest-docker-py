#!/usr/bin/env bash

export PYTHONPATH=src:$PYTHONPATH
pytest -s --cov-report term-missing --cov . test/unit
mkdir coverage
mv .coverage coverage/.coverage.0

pip install git+https://github.com/jameshnsears/pytest-docker-py@master
pytest -s --junitxml --cov-report term-missing --cov . test/integration
mv .coverage coverage/.coverage.1
cd coverage
coverage combine
coverage xml -i
