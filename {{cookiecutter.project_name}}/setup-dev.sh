#!/bin/bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install --editable .
cp .env.example .env
cp .env backend/src/backend/.env
