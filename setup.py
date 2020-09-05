import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ulia-DanielUhl",
    version="1.0.0",
    author="Daniel Uhl",
    author_email="daniel_uhl@hotmail.de",
    description="Software based simulation of a Lock-In amplifier.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.sauerburger.com/saeuble/ulia",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
