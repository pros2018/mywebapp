# Use the official Python image as a base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Set up a virtual environment
RUN python -m venv venv
RUN /bin/bash -c "source venv/bin/activate"

# Install Flask
RUN pip install --no-cache-dir Flask

# Expose port 7001 to the outside world
EXPOSE 7001

# Define environment variables
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=7001"]
