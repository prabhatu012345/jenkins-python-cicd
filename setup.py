# setup.py
from setuptools import setup, find_packages

setup(
    name='hello_world',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hello=hello_world.hello:say_hello',
        ],
    },
    install_requires=[],
    tests_require=['pytest'],
    test_suite='tests',
)
