import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ulia",
    version="2021.09.2",
    packages=["ulia", "ulia.tests"],
    install_requires=['numpy>=1.14', 'scipy>=1.4', 'numba>=0.52'],
    test_suite="ulia.tests",
    maintainer="Daniel Uhl",
    maintainer_email="daniel_uhl@hotmail.de",
    author="Daniel Uhl",
    author_email="daniel_uhl@hotmail.de",
    description="Algorithm to emulate a lock-in amplifier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="lia lock-in amplifier",
    license="MIT",
    url="https://gitlab.com/UhlDaniel/ulia",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
