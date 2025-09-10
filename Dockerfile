FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir --progress-bar off websockets

COPY main.py .

EXPOSE 8765

CMD ["python", "main.py"]
