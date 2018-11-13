import logging

import pytest

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)

logging.getLogger('flake8').setLevel(logging.WARNING)
logging.getLogger('docker').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)


def test_hello_default(hello):
    assert hello() == "Hello World!"


@pytest.fixture(params=[
    "Brianna",
    "Andreas",
    "Floris",
])
def name(request):
    return request.param


def test_hello_name(hello, name):
    assert hello(name) == "Hello {0}!".format(name)
