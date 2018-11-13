import logging

import pytest

from pytest_docker_py.config import Config
from pytest_docker_py.docker_py_wrapper import DockerPyWrapper

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d  %(levelname)8s --- [%(process)5d] %(filename)25s:%(funcName)30s, %(lineno)3s: %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
    level=logging.DEBUG)

logging.getLogger('docker').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)

docker_py_wrapper = DockerPyWrapper()


@pytest.fixture
def configuration():
    return Config([{'image': 'alpine:latest',
                    'name': 'alpine-01',
                    'ports': {'1234/tcp': 1234},
                    'volumes': ['alpine-01:/tmp'],
                    'command': 'sleep 12345'},
                   {'image': 'busybox:latest',
                    'name': 'busybox-01',
                    'network': 'docker_py_wrapper'}
                   ])


def test_configuration(configuration):
    assert configuration.images() == ['alpine:latest', 'busybox:latest']
    assert configuration.networks() == ['docker_py_wrapper']


@pytest.mark.timeout(30)
def test_pull_images(configuration):
    docker_py_wrapper.rm_images(configuration.images())
    for configuration_image in configuration.images():
        assert configuration_image not in docker_py_wrapper.ls_images()

    docker_py_wrapper.pull(configuration.images())
    for configuration_image in configuration.images():
        assert configuration_image in docker_py_wrapper.ls_images()


def test_stop_start_containers(configuration):
    docker_py_wrapper.start_containers(configuration)
    assert len(docker_py_wrapper.ls_containers(configuration.images())) == 2
    assert docker_py_wrapper.ls_networks(configuration.networks()) == ['docker_py_wrapper']
    assert docker_py_wrapper.ls_volumes(configuration.volumes()) == ['alpine-01:/tmp']

    docker_py_wrapper.rm_containers(configuration.images())
    assert docker_py_wrapper.ls_containers(configuration.images()) == []
    assert docker_py_wrapper.ls_networks(configuration.networks()) == []
    assert docker_py_wrapper.ls_volumes(configuration.volumes()) == []
