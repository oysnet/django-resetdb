#!/usr/bin/env python
from setuptools import setup, find_packages

import dbsync

CLASSIFIERS = [
    'Intended Audience :: Developers',    
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python'    
]

KEYWORDS = 'django syncdb innodb mysql drop table'


setup(name = 'mailsnake',
    version = dbsync.__version__,
    description = """Add ability to drop tables before syncdb""",
    author = dbsync.__author__,
    url = "https://github.com/oxys-net/django-dbsync",
    packages = find_packages(),
    classifiers = CLASSIFIERS,
    keywords = KEYWORDS,
    zip_safe = True
)