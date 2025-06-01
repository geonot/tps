# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# Using --no-cache-dir to reduce image size and virtualenv for isolation (optional but good practice)
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variables
ENV FLASK_APP app.py
ENV FLASK_ENV development # Change to production for real deployments
# Ensures commands like 'flask' use the venv
ENV PATH="/opt/venv/bin:$PATH"

# Command to run the application.
# For development, Flask's built-in server is fine.
# For production, Gunicorn is recommended.
# The example below uses Flask's server. If using Gunicorn, ensure it's in requirements.txt.
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
# To use Gunicorn (ensure it's in requirements.txt):
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
