# Dockerfile
FROM python:3.10-slim

# Seting working directory to app
WORKDIR /app

#Code for installing dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
