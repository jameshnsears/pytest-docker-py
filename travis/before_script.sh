#!/usr/bin/env bash

pip install --upgrade pip
pip install -r requirements.txt
flake8 src test
pylint --rcfile=setup.cfg src test -r n --msg-template='{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}' > pylint-report.txt
