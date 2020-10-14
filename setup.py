"""Setup file."""

import setuptools  # type: ignore

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WarCardGame",
    version="0.1.2",
    author="Kamil Grula",
    author_email="kamilgrula@gmail.com",
    description="War - card game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TODO",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
