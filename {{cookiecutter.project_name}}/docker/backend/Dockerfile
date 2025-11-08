FROM python:3.12-slim

WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
COPY backend/ ./backend/
RUN pip install --upgrade pip \
    && pip install --editable ./backend
WORKDIR /app/backend/src/backend

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "api.wsgi"]
