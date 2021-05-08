#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""The setup script."""


from setuptools import setup, find_packages


with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
    "sqlparse>=0.4",
]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]


setup(
    python_requires=">=3.5",
    name="cleanql",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    setup_requires=setup_requirements,
    entry_points={"console_scripts": ["cleanql = cleanql:cli"]},
    test_suite="tests",
    tests_require=test_requirements,
)
