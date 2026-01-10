# Menggunakan Python 3.11 slim sebagai base image
FROM python:3.11-slim

# Set working directory di dalam container
WORKDIR /app

# Install psutil untuk monitoring resource
RUN pip install --no-cache-dir psutil

# Copy program ke dalam container
COPY app.py .

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Jalankan aplikasi
CMD ["python", "app.py"]