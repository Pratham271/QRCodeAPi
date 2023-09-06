# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 (the port your Flask app will run on)
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
