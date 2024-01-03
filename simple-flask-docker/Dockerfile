FROM python:3.9.4-slim


WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app code
COPY . .

# Expose app port
EXPOSE 8000

VOLUME /app/data

# Run app on port 8000
CMD ["gunicorn", "app:app", "--bind=0.0.0.0:8000"]
