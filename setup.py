#!/usr/bin/env python

from setuptools import setup
import doctest

MODULE = 'mdx_figcap'

tests = lambda: doctest.DocTestSuite(MODULE)

setup(
    name=MODULE,
    version='1.3',
    description='Figure Caption extension for Python-Markdown.',
    long_description_markdown_filename='README.md',
    py_modules=[MODULE],
    install_requires=['Markdown'],
    license='The BSD 2-Clause License',
    keywords='markdown figure caption',
    classifiers=[]
)
