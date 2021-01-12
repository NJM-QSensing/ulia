#!/bin/bash

pip install twine
python3 -m twine upload --skip-existing --sign dist/*
