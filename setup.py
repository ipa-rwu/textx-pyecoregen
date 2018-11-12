#!/usr/bin/env python
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

if sys.version_info < (3, 3):
    sys.exit('Sorry, Python < 3.3 is not supported')


setup(
    name="textx_pyecoregen",
    version='0.0.1',
    description="Model to text framework for PyEcore, including the Ecore to Python generator",
    keywords="model metamodel EMF Ecore code generator textX",
    url="https://github.com/pyecore/pyecoregen",

    packages=find_packages(),
    package_data={'textx_pyecoregen': ['templates/*']},
    include_package_data=True,
    install_requires=['pyecore', 'pymultigen', 'jinja2', 'autopep8'],
    entry_points={'console_scripts': ['textx-pyecoregen = textx_pyecoregen.cli:main']},

    license='BSD 3-Clause',
    classifiers=[
        "Development Status :: POC",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: BSD License",
    ]
)
