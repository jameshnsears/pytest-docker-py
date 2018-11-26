import docker
import pytest


@pytest.fixture
def dockerpy():
    return [{'image': 'alpine:latest',
             'name': 'alpine-01',
             'ports': {'1234/tcp': 1234},
             'volumes': {'alpine-01': {'bind': '/tmp', 'mode': 'rw'}},
             'network': 'alpine-01',
             'command': 'sleep 30'}
            ]


@pytest.mark.timeout(60)
def test_plugin(dockerpy):
    """
    For each test_ def, when a fixture starting with 'dockerpy' is supplied, the plugin overrides pytest's setup and teardown.

    pytest_runtest_setup = will pull / start container(s).
    pytest_runtest_teardown = will kill container(s).
    """
    client = docker.from_env()
    for container in client.containers.list():
        for tag in container.image.tags:
            assert tag == 'alpine:latest'
