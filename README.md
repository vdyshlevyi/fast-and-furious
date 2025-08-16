# Fast & Furious

![CI](https://github.com/vdyshlevyi/fast-and-furious/actions/workflows/ci.yml/badge.svg)
[![codecov](https://codecov.io/gh/vdyshlevyi/fast-and-furious/branch/main/graph/badge.svg)](https://codecov.io/gh/vdyshlevyi/fast-and-furious)



This repository contains the simple FastAPI app.

## Prerequisites

Before getting started, ensure the following tools are installed:

* [pyenv](https://github.com/pyenv/pyenv)
* [Docker](https://www.docker.com/)
* [wget](https://www.gnu.org/software/wget/)

---

## 1. Clone the repository:
```bash
git clone https://github.com/vdyshlevyi/fast-and-furious
cd fast-and-furious
```

## 2. Local development
### Install requirements via poetry:
```bash
make setup
```

### Activate the virtual environment:
```bash
source venv/bin/activate
# or
. venv/bin/activate
```

### Copy and fill .env file:
```bash
cp .env_example .env
```

### Start DEV server:
```bash
make run
```
---

## Usefully checks
### Check code style(ruff):
```bash
make lint
```

### Check types:
```bash
make mypy
```

### Run tests:
```bash
make test
```

### Tests coverage:
```bash
make coverage
```

---
## Docker
### Build Docker image:
```bash
docker build --no-cache -t fast_and_furious:0.1.0 .
```

### Check that the image was created:
```bash
docker image ls | grep fast_and_furious
```

### Run via Docker
```bash
docker run --name fast_and_furious -e HOST=0.0.0.0 -e SECRET_KEY=1234567890 -itd -p 9000:9000 fast_and_furious:0.1.0
```
