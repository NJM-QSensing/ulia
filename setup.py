import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ulia",
    maintainer="Daniel Uhl",
    maintainer_email="daniel_uhl@hotmail.de",
    version="1.0.3",
    author="Daniel Uhl",
    author_email="daniel_uhl@hotmail.de",
    description="Package contains an algorithm to simulate a lock-in amplifier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/UhlDaniel/ulia",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

