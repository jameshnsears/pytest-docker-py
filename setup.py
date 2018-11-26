from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pytest-docker-py",
    description="Easy to use, simple to extend, pytest plugin that minimally leverages docker-py.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="1.1.1",
    author="James Sears",
    author_email="james.hn.sears@gmail.com",
    url="https://github.com/jameshnsears/pytest-docker-py",
    license="Apache 2.0",
    packages=["pytest_docker_py"],
    package_dir={"": "src"},
    install_requires=[
        "pytest==4.0.0",
        "docker==3.5.1"
    ],
    keywords="pytest plugin docker-py",
    entry_points={"pytest11": ["pytest-docker-py = pytest_docker_py.plugin"]},
    classifiers=["Framework :: Pytest",
                 "Programming Language :: Python :: 3.6",
                 "Topic :: Software Development :: Testing",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: Apache Software License"
                 ],
)
