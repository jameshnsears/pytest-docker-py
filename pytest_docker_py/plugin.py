import logging

import pytest

from pytest_docker_py.docker_py_wrapper import DockerPyWrapper


def pytest_addoption(parser):
    parser.addoption(
        "--pytest-docker-py",
        action="store",
        dest="name",
        default="World",
        help='Default "name" for hello().',
    )


@pytest.fixture
def hello(request):
    try:
        name = request.config.getoption("name")
    except ValueError:
        name = None

    def _hello(name=None):
        if not name:
            name = 'World'
        return "Hello {name}!".format(name=name)

    return _hello


docker_wrapper = DockerPyWrapper()


def pytest_runtest_setup(item):
    logging.debug("setup: %s", item)
    docker_wrapper.images_to_pull(['jameshnsears/xqa-db:latest',
                                   'jameshnsears/xqa-message-broker:latest'])


def pytest_runtest_teardown(item, nextitem):
    logging.debug("teardown: %s; %s", item, nextitem)
    # shutdown containers
