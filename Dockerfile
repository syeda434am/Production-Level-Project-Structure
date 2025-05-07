# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1


# Install required packages and dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    musl-dev \
    net-tools \
    nginx \
    build-essential \
    libffi-dev \
    libssl-dev \
    python3-dev \
    make


# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies with limited parallel builds
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Copy Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Run the Gunicorn server and Nginx
CMD ["sh", "-c", "gunicorn -c gunicorn_config.py com.mhire.app.main:app & nginx -g 'daemon off;'"]
