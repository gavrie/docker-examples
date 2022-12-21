# Use full image for build
FROM python:3.10.4-bullseye as build

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

####################################################

# Use slim image for deployment
FROM python:3.10.4-slim-bullseye

# Create user and switch to it
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# Use the previously built virtualenv
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY --from=build /opt/venv /opt/venv

# App
COPY myapp.py .
CMD ["python", "myapp.py"]
