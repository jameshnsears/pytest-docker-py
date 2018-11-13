import json
import logging

import docker
import pytest

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d  %(levelname)8s --- [%(process)5d] %(filename)25s:%(funcName)30s, %(lineno)3s: %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
    level=logging.DEBUG)

logging.getLogger('docker').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)


@pytest.fixture
def dockerpy():
    return [{'image': 'alpine:latest',
             'name': 'alpine-01',
             'ports': {'1234/tcp': 1234},
             'volumes': ['alpine-01:/tmp'],
             'network': 'alpine-01',
             'command': 'sleep 30'}
            ]


def test_plugin(dockerpy):
    """
    For each test_ def, when a fixture starting with 'dockerpy' is supplied, the plugin overrides pytest's setup and teardown.

    pytest_runtest_setup = will pull / start a container.
    pytest_runtest_teardown = will kill the container.
    """
    client = docker.from_env()
    for container in client.containers.list():
        for tag in container.image.tags:
            logging.info('%s: %s - %s' % (tag, container.id, json.dumps(container.attrs['NetworkSettings']['Ports'])))
