# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'seer',
    version = '1.0.1',
    keywords = ('seer', 'api', 'sdk'),
    description = 'Python SDK for SEER API',
    url = 'https://github.com/seer-project/seer-py',
    packages = find_packages(),
    install_requires = [
        'requests',
    ],
    author = '0xDAI',
    author_email = 'seer@nsfocus.com',
)
