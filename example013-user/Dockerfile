FROM python:3.10-slim-bullseye

# Create user and switch to it
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# App
COPY myapp.py .
CMD ["python", "myapp.py"]
