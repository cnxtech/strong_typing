#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

CONTAINING_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

package_list = find_packages(where=CONTAINING_DIRECTORY)

setup(
    name='strong_typing',
    version=open(os.path.join(CONTAINING_DIRECTORY,"strong_typing/VERSION")).read().split()[0],
    description='Classes to create strongly typed structures in Python',
    long_description=open(os.path.join(CONTAINING_DIRECTORY,'README.rst')).read(),
    url='https://gitlab.aldebaran.lan/sambrose/py_strong_typing',
    author='Surya Ambrose',
    author_email='sambrose@softbankrobotics.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    keywords='static-typing strongly-typed structures',
    packages=package_list,
    install_requires=[
        # 'enum34;python_version<"3.4"', not recognized by old setuptools ?
        "enum34 >= 1.0.4"
    ],
    package_data={
        "strong_typing":["VERSION", "../README.rst"]
    }
)