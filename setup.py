#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup


setup(
    name='feincms-tinymce',
    version='0.0.1',
    description='Tiny MCE plugin for FeinCMS',
    author='',
    author_email='',
    long_description=open('README.md', 'r').read(),
    packages=[
        'feincms_tinymce'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    zip_safe=False,
)
