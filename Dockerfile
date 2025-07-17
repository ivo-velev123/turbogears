FROM python:3.14.0b4-slim-bookworm

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3","tgapp.py"]

EXPOSE 8080