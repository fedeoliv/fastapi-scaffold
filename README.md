# FastAPI Scaffold

Core features:

- [uv](https://docs.astral.sh/uv/) for package and project management;
- App settings management and type validations from `.env` with [pydantic](https://pypi.org/project/pydantic/) and [pydantic-settings](https://pypi.org/project/pydantic-settings/);
- FastAPI with app settings integrated into an API route via [dependency injection](https://fastapi.tiangolo.com/tutorial/dependencies/).

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) for package and project management

### Build and run from source

Create a virtual environment:

```sh
   uv venv
```

Activate the virtual environment:

   <details>
       <summary>Linux/macOS</summary>

```
source .venv/bin/activate
```

   </details>

   <details>
       <summary>Windows</summary>

```
.venv\Scripts\Activate
```

   </details>

Install dependencies:

```
uv sync
```

Run the API:

```
fastapi dev app/main.py
```

### Build and run as Docker container

Build the image:

```sh
docker build -t fastapi-app .
```

Run the container:

- Option 1: Run with the `.env` file:
  ```sh
  docker run --env-file .env --rm -d --name fastapi-app-container -p 8001:80 fastapi-app
  ```
- Option 2: Run by injecting env variables manually with `-e`:

  ```sh
  docker run -e MY_ENV=VALUE -e MY_OTHER_ENV=VALUE --rm -d --name fastapi-app-container -p 8001:80 fastapi-app
  ```
