# Static code analysis and running tests scripts.

# pip3 install .
pytest --cov war --cov tests tests/ --cov-report term-missing

echo "PYLINT:"
pylint war setup.py main.py
pylint tests --disable=C0116

echo "MYPY:"
mypy .
