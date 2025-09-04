FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install gunicorn

COPY . .

EXPOSE 8000

CMD ["gunicorn", "MessageBoard.wsgi:application", "--bind", "0.0.0.0:8000"]