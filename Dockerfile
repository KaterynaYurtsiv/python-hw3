FROM python:3.12-slim

WORKDIR /app

COPY Task3.py .

CMD ["python", "Task3.py"]
