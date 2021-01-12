#!/bin/bash

pip install twine
twine upload --skip-existing --sign dist/*
