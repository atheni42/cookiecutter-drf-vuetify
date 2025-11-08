#!/bin/bash
source backend/.venv/bin/activate
python -m flake8 --config=linters/flake8.ini backend/src/backend
python -m black backend/src/backend
python -m isort backend/src/backend
