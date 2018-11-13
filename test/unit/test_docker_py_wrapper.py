import pytest

from docker_py_wrapper import DockerPyWrapper


@pytest.mark.timeout(30)
def test_docker_py_wrapper():
    docker_py_wrapper = DockerPyWrapper()
    assert docker_py_wrapper.images_to_pull([]) is None
