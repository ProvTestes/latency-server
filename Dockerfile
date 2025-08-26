FROM python:3.9-slim

WORKDIR /app

RUN pip install websockets

COPY main.py .

EXPOSE 8765

CMD ["python", "main.py"]