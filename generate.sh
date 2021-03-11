#!/bin/bash
#python setup.py sdist bdist_wheel
pip install "dist/$(ls dist/ | grep whl)"

python -m twine uplaod --repository-url https://test.pypi.org/legacy/ dist/*

python -m twine uplaod --repository-url https://upload.pypi.org/legacy/ dist/*
