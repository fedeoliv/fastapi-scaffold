# FastAPI Scaffold

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

```sh
docker run -d --name fastapi-app-container -p 8000:80 fastapi-app
```

```

```
