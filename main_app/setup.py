#!/usr/bin/env python

from setuptools import setup


setup(
    name='main_app',
    version='1.0',
    author='Me',
    description="Namespace plugin testing main app",
    packages=['main_app', 'main_app.plugins'],
    entry_points = {'console_scripts': [
        'main_app = main_app.__main__:main'
    ]}
)