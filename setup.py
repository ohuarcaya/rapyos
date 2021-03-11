from setuptools import find_packages, setup

setup(
    name='rapyos',
    packages=find_packages(include=[
        'rapyos'
        ]),
    version='0.1.1',
    description='My first Python library',
    author='Oscar Huarcaya',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests'
)
