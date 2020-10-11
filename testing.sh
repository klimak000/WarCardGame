
# pip3 install .
pylint war setup.py
pylint tests --disable=C0116
mypy .
pytest --cov=war tests/ --cov-report term-missing