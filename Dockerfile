# Use an official Python image as the base image
FROM python:3.12

# Add Microsoft package signing key and repository
RUN curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc
# RUN curl https://packages.microsoft.com/config/debian/10/prod.list | tee /etc/apt/sources.list.d/mssql-release.list

# # Update package lists
# RUN apt-get update

# # Install msodbcsql18 and unixodbc-dev
# RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18
# RUN apt-get install -y unixodbc-dev

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code to the container
COPY . .

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=talentfinder.settings

# Expose port 8000 for the Django app
EXPOSE 8000

# Define the command to run the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
