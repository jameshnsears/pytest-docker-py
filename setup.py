from setuptools import setup

setup(
    name="pytest-docker-py",
    description='pytest plugin to minimally leverage docker-py',
    license="Apache 2",
    version='1.0.0',
    author='James Sears',
    author_email='james.hn.sears@gmail.com',
    url='https://github.com/jameshnsears/pytest-docker-py',
    packages=["pytest_docker_py"],
    install_requires=[
        'pytest==3.6.3',
        'docker==3.5.1'
    ],
    entry_points={"pytest11": ["pytest-docker-py = pytest_docker_py.plugin"]},
    classifiers=["Framework :: Pytest",
                 'Programming Language :: Python :: 3.6',
                 'Topic :: Software Development :: Testing',
                 ],
)
