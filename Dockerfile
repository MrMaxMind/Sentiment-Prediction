# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create a virtual environment in the container
RUN python -m venv venv

# Activate the virtual environment and install dependencies
RUN . /app/venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# Ensure the virtual environment is used when running commands
ENV PATH="/app/venv/bin:$PATH"

# Define environment variable
ENV FLASK_ENV=production

# Expose port 5000 for Flask
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
