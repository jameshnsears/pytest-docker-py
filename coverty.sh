#!/usr/bin/env bash

export PATH=${HOME}/bin/cov-analysis-linux64-2017.07/bin:${PATH}

cov-build --dir cov-int --no-command --fs-capture-search ./

tar czvf jameshnsears_pytest-docker-py.tgz cov-int

# https://scan.coverity.com/projects/jameshnsears-pytest-docker-py?tab=project_settings
export COVERITY_SCAN_TOKEN=

curl --form token=${COVERITY_SCAN_TOKEN} --form email=james.hn.sears@gmail.com --form file=@jameshnsears_pytest-docker-py.tgz --form version="HEAD" --form description="jameshnsears_pytest-docker-py.tgz" https://scan.coverity.com/builds?project=jameshnsears%2Fpytest-docker-py
