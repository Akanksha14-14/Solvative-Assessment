# Using Apache
FROM ubuntu:latest

# Update package list and install Apache2
RUN apt-get update && apt-get install -y apache2

# Create a sample HTML file
RUN echo "<html><body><h1>Hello from Apache!</h1></body></html>" > /var/www/html/index.html

# Expose port 80
EXPOSE 80

# Start Apache when container starts
CMD ["apache2ctl", "-D", "FOREGROUND"]
