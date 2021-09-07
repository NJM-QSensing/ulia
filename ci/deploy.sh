#!/bin/bash

pip install twine anybadge
python3 -m twine upload --skip-existing dist/*

pip install .
anybadge -o --color "#006dad" -l PyPI -v $(python3 -c "import ulia; print(ulia.__version__)") -f pypi.svg
