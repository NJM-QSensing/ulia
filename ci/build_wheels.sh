#!/bin/bash

python3 setup.py bdist_wheel

pip install anybadge numpy scipy numba
pip install .
anybadge -o --color "#006dad" -l PyPI -v $(python3 -c "import ulia; print(ulia.__version__)") -f pypi.svg
