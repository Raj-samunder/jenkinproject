# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy the Python script into container
COPY acronym.py .

# Run the Python script
CMD ["python", "acronym.py"]
