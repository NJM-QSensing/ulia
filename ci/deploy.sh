#!/bin/bash

echo "$GPG_KEY" | gpg --import

pip install twine
python3 -m twine upload --skip-existing --sign dist/*
