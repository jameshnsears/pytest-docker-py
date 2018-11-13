# pytest-docker-py [![Build Status](https://travis-ci.org/jameshnsears/pytest-docker-py.svg?branch=master)](https://travis-ci.org/jameshnsears/pytest-docker-py) [![Coverage Status](https://coveralls.io/repos/github/jameshnsears/pytest-docker-py/badge.svg?branch=master)](https://coveralls.io/github/jameshnsears/pytest-docker-py?branch=master)
* pytest plugin to minimally leverage docker-py

## 1. Ubuntu 18.04 Install Requirements
* sudo apt-get install -y python3-pip python3-venv

## 2. Set up working dir
* git clone https://github.com/jameshnsears/pytest-docker-py.git /tmp/pytest-docker-py
* cd /tmp/pytest-docker-py

## 3. Unit Tests
* python3 -m venv venv-00
* source venv-00/bin/activate
* pip install -r requirements.txt
* export PYTHONPATH=pytest_docker_py:$PYTHONPATH
* pytest -s --flake8 --cov-report term-missing --cov . test/unit
* deactivate

## 4. Integration Tests / plugin Install
* cd /tmp
* python3 -m venv venv-01
* source venv-01/bin/activate
* pip install git+https://github.com/jameshnsears/pytest-docker-py@master
* pytest -s --flake8 --cov-report term-missing --cov . test/integration
