FROM python:3.12-slim-bullseye

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy the app into the container
COPY . /app

# Install dependencies
WORKDIR /app
RUN uv sync --frozen --no-cache

# Run the app
CMD ["/app/.venv/bin/fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "80"]
