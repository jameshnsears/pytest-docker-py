## Register on PyPi
* https://test.pypi.org/account/register/
* https://pypi.org/account/register/

## Package
* each upload requires a new version, in setup.py

## Publish
* ./publish.sh
* visit https://test.pypi.org/manage/projects/

## Test - test.pypi.org
* export VENV=venv-pytest-docker-py
* python3 -m venv $VENV
* source $VENV/bin/activate
* pip install --extra-index-url https://test.pypi.org/simple/ pytest-docker-py
* git clone https://github.com/jameshnsears/pytest-docker-py
* pytest -s pytest-docker-py/test/integration
