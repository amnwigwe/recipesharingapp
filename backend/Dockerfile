FROM python:3.11-slim

# Install build dependencies for MySQL connector
RUN apt-get update && \
    apt-get install -y gcc libffi-dev libssl-dev default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY . .

# Set working directory to app/ (where main.py lives)
WORKDIR /app/app

# Run the backend
CMD ["python", "main.py"]
