# coding: utf-8
# flake8: noqa


from setuptools import find_packages
from setuptools import setup


setup(
    name='randomness',
    version='0.1.0',
    description='A small set of examples to demonstrate randomness in Python',
    author='Cody Lane',
    author_email='cody.lane@gmail.com',
    url='https://github.com/codylane/python-randomness',
    packages=find_packages(
        'src',
        exclude=["*.tests"]
    ),
    package_dir={
        "": "src",
    },
    long_description='A small set of examples to demonstrate randomness in Python',
    tests_require=[],
    install_requires=[],
    zip_safe=False,
    entry_points={},
    scripts=[]
)

