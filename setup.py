from setuptools import setup
from setuptools import find_packages

try:
    with open("README.md") as f:
        long_description = f.read()
except IOError:
    long_description = ""


try:
    with open("dev_requirements.txt") as f:
        requirements = [x.strip()
                        for x in f.read().splitlines() if x.strip()]
except IOError:
    requirements = []


setup(
    name="first_spark_boilreplate",
    author="ouss",
    version="1.0.0",
    author_email="ouss.miss@gmail.com",
    description="demo spark pkg",
    long_description=long_description,
    install_requires=requirements,
    packages=find_packages(exclude=("tests",)),
    package_data={
        "src": ["data/*.csv"]
    },

)
