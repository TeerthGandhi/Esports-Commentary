FROM python:3.11.4

# Prevents Python from writing .pyc files and enables unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install essential system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    zlib1g-dev && \
    apt-get clean

# Set up the working directory
RUN mkdir /code
WORKDIR /code

# Upgrade pip and install dependencies separately to utilize Docker's layer caching
RUN pip install --upgrade pip

# Copy requirements file and install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the application code
COPY . /code/

# Expose the port that Django will run on
EXPOSE 8000

# Add a health check to verify that the server is running
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/ || exit 1

# Run the Django development server on port 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
