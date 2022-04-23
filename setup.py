import os
import setuptools
from setuptools import setup, find_packages

setup(
    name="qthread",
    version="0.0.1",
    description="Python library for using threads",
    python_requires=">=3.6",
    author="Adam Frank",
    author_email="pkgmaint@antilogo.org",
    packages=find_packages(),
    project_urls={"Source": "https://github.com/afrank/qthread",},
)

