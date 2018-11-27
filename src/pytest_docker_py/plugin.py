import logging
import os

from pytest_docker_py.config import Config
from pytest_docker_py.docker_py_wrapper import DockerPyWrapper


# noinspection PyProtectedMember
def pytest_runtest_setup(item):
    logging.debug("setup: %s", item)
    for fixturename in item.fixturenames:
        if fixturename.startswith(DockerPyWrapper.RECOGNISED_FIXTURE):
            docker_py_wrapper = DockerPyWrapper()
            # no alternative, at moment, other than using ._request
            config = Config(item._request.getfixturevalue(fixturename))
            docker_py_wrapper.rm_containers(config.images())
            if docker_py_wrapper.pull(config.images()):
                docker_py_wrapper.start_containers(config)


# noinspection PyUnusedLocal,PyProtectedMember
def pytest_runtest_teardown(item, nextitem):
    logging.debug("teardown: %s", item)
    if "PYTEST_DOCKER_PY_KEEP_LOGS" not in os.environ:
        for fixturename in item.fixturenames:
            if fixturename.startswith(DockerPyWrapper.RECOGNISED_FIXTURE):
                docker_py_wrapper = DockerPyWrapper()
                docker_py_wrapper.rm_containers(
                    Config(item._request.getfixturevalue(fixturename)).images())
