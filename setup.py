#!/usr/bin/env python
from setuptools import setup, find_packages

import resetdb

CLASSIFIERS = [
    'Intended Audience :: Developers',    
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python'    
]

KEYWORDS = 'django syncdb innodb mysql drop table'


setup(name = 'resetdb',
    version = resetdb.__version__,
    description = """Add ability to drop tables before syncdb""",
    author = resetdb.__author__,
    url = "https://github.com/oxys-net/django-resetdb",
    packages = find_packages(),
    classifiers = CLASSIFIERS,
    keywords = KEYWORDS,
    zip_safe = True
)