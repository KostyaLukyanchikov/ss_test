FROM python:3.10

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install 'poetry==1.3.2'

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

COPY . /app

# If running behind a proxy like Nginx or Traefik add --proxy-headers
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8080", "--proxy-headers", "--timeout-keep-alive", "0"]