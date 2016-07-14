# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='aws-ip-ranges',
    version='0.0.1',
    description='AWS Public IP Address Ranges command line tool',
    long_description=readme,
    author='Marcus Vinicius Ferreira',
    author_email='ferreira.mv@gmail.com',
    url='https://github.com/mv/aws-ip-ranges',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

