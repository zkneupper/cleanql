#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""The setup script."""


from setuptools import setup, find_packages


requirements = [
    "Click>=7.0",
]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]


setup(
    python_requires=">=3.5",
    name="sql_formatter",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    setup_requires=setup_requirements,
    entry_points={"console_scripts": ["cleanql = sql_formatter:cli"]},
    test_suite="tests",
    tests_require=test_requirements,
)
