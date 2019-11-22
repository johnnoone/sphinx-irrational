#!/usr/bin/env python

import codecs
from setuptools import setup

# Version info -- read without importing
_locals = {}
with open('irrational/_version.py') as fp:
    exec(fp.read(), None, _locals)
version = _locals['__version__']

# README into long description
with codecs.open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='irrational',
    version=version,
    description='A configurable sidebar-enabled Sphinx theme',
    long_description=readme,
    author='Xavier Barbosa',
    author_email='clint.northwood@gmail.com',
    url='http://sphinx.errorist.io/irrational',
    packages=['irrational'],
    package_data = {'irrational': [
        'theme.conf',
        'layout.html',
        'static/*.*',
     ]},
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points = {
        'sphinx_themes': [
            'path = irrational:get_path',
        ],
        'sphinx.html_themes': [
            'irrational = irrational',
        ]
    },
)
