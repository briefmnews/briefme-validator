#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of briefme-validator.
# https://github.com/briefmnews/briefme-validator

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Hobbestigrou <hobbestigrou@erakis.eu>

from setuptools import setup, find_packages

tests_require = [
    "mock",
    "nose",
    "coverage",
    "yanc",
    "preggy",
    "tox",
    "ipdb",
    "coveralls",
    "sphinx",
]

setup(
    name="briefme-validator",
    version="0.1.3",
    description="A simple validator.",
    long_description="""A simple validator, check mail for example.""",
    keywords="dns, mail",
    author="Hobbestigrou",
    author_email="hobbestigrou@erakis.eu",
    url="",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=["dnspython"],
    entry_points={"console_scripts": []},
)
