"""Setup file."""

import setuptools  # type: ignore

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WarCardGame",
    version="0.3.1",
    author="Kamil Grula",
    author_email="kamilgrula@gmail.com",
    description="War - card game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/klimak000/WarCardGame",
    packages=setuptools.find_packages(),
    scripts=['war_card_game_test.py'],
    install_requires=['pylint', 'mypy', 'pytest', 'pytest-cov'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
