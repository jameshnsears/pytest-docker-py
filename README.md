# pytest-docker-py [![Build Status](https://travis-ci.org/jameshnsears/pytest-docker-py.svg?branch=master)](https://travis-ci.org/jameshnsears/pytest-docker-py) [![Coverage Status](https://coveralls.io/repos/github/jameshnsears/pytest-docker-py/badge.svg?branch=master)](https://coveralls.io/github/jameshnsears/pytest-docker-py?branch=master)
* Easy to use, simple to extend, external [pytest](https://docs.pytest.org/en/latest/) plugin that minimally leverages [docker-py](https://github.com/docker/docker-py).

## 1. Introduction
* A plugin that keeps it simple and lets you:
    * pull images - if not already pulled.
    * start containers - with various, optional, parameters - i.e. ports; networks; volumes; commands.
    * stop containers.

* See [test/integration/test_plugin.py](https://github.com/jameshnsears/pytest-docker-py/blob/master/test/integration/test_plugin.py) for a working example.

## 2. Installation
* pip install pytest-docker-py

or

* pip install git+https://github.com/jameshnsears/pytest-docker-py@master

then
* create a test, similar to [test/integration/test_plugin.py](https://github.com/jameshnsears/pytest-docker-py/blob/master/test/integration/test_plugin.py)
* run pytest -s 

## 3. Development / PR - on Ubuntu 18.04
* sudo apt-get install -y build-essential python3-pip python3-venv
* git clone https://github.com/jameshnsears/pytest-docker-py.git 
* cd pytest-docker-py

### 3.1. Create Virtual Environment
* ./create-venv.sh

### 3.2. Unit Tests
* ./run-unit-tests.sh

### 3.3. Integration Tests
* ./run-integration-tests.sh
