# Use the official Python image as a base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Set up a virtual environment and install Flask
RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir Flask

# Expose port 7001 to the outside world
EXPOSE 7001

# Run the Flask application using the Python interpreter
CMD ["venv/bin/python", "mywebapp.py"]
