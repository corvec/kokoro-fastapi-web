# This should match the version specified in the .python-version file
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy just the requirements file first to leverage Docker cache
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the image
COPY . .

# Expose port 7860 for the Gradio interface
EXPOSE 7860

# Set the default command to launch the app
CMD ["python", "app.py"]
