#!/usr/bin/env bash

rm -rf dist src/pytest_docker_py.egg-info
source venv-00/bin/activate
python3 setup.py sdist bdist_wheel
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
