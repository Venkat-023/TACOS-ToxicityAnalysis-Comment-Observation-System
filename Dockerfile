FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=7860 \
    API_PORT=8000

WORKDIR /app

COPY requirements-docker.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements-docker.txt

COPY Backend ./Backend
COPY Frontend ./Frontend
COPY start.py ./start.py
COPY README.md ./README.md

EXPOSE 7860

CMD ["python", "start.py"]
