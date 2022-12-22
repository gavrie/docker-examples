FROM python:3.10.4-slim-bullseye

# Install poetry globally
RUN pip install poetry==1.3.1
RUN poetry --version

# Create virtualenv for deployment
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry install

# App
COPY myapp.py .
CMD ["python", "myapp.py"]
