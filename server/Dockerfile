FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# COPY requirements.txt .
COPY server/requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY server/ ./server

CMD ["python", "-m", "server.app"]