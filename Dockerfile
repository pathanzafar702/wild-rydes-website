FROM python:3.9-slim-buster  # Use a slim Python image

WORKDIR /app

COPY requirements.txt .  # Copy requirements first for caching
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
