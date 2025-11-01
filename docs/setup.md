# Setup & Installation Guide

## Prerequisites

- Python 3.10 or higher
- pip and virtualenv
- Git
- (Optional) Docker and Docker Compose

## Installation Methods

### 1. Local Development Setup

#### Step 1: Clone the Repository

```bash
git clone https://github.com/overandor/champ-lm.git
cd champ-lm
```

#### Step 2: Create Virtual Environment

```bash
# On macOS/Linux
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

#### Step 3: Install Dependencies

```bash
# Development setup (includes testing tools)
pip install -e ".[dev]"

# Or production only
pip install -r requirements.txt
```

#### Step 4: Configure Environment

```bash
cp .env.example .env
# Edit .env with your values
nano .env
```

#### Step 5: Verify Installation

```bash
# Run tests
pytest tests/ -v

# Or start the dashboard
streamlit run src/api/dashboard.py
```

### 2. Docker Setup

#### Step 1: Prerequisites

Ensure Docker and Docker Compose are installed:

```bash
docker --version
docker-compose --version
```

#### Step 2: Build and Start Services

```bash
docker-compose up --build
```

#### Step 3: Access Services

- Dashboard: http://localhost:8501
- Metrics: http://localhost:9090

### 3. Editable Installation from GitHub

```bash
pip install git+https://github.com/overandor/champ-lm.git@main#egg=champ-lm
```

## Development Tools Setup

### Pre-commit Hooks

```bash
pip install pre-commit
pre-commit install

# Run hooks manually
pre-commit run --all-files
```

### Code Formatting

```bash
# Auto-format code
black src tests
isort src tests

# Check formatting
black --check src tests
```

### Linting & Type Checking

```bash
# Lint
flake8 src tests

# Type check
mypy src --ignore-missing-imports
```

## Common Issues

### Issue: "Python version not supported"

**Solution:** Install Python 3.10+
```bash
# Ubuntu/Debian
sudo apt install python3.11

# macOS
brew install python@3.11
```

### Issue: "Permission denied" on virtual environment

**Solution:** Use explicit Python executable
```bash
/usr/bin/python3.11 -m venv venv
```

### Issue: Port 8501 already in use

**Solution:** Use different port
```bash
streamlit run src/api/dashboard.py --server.port 8502
```

### Issue: Model download fails in Docker

**Solution:** Pre-pull models manually
```bash
docker exec champ-lm-llama3-8b-1 ollama pull llama2
docker exec champ-lm-mistral-7b-1 ollama pull mistral
```

## Next Steps

1. Read [DEPLOYMENT.md](../DEPLOYMENT.md) for production setup
2. Check [CONTRIBUTING.md](../CONTRIBUTING.md) for development guidelines
3. Review [README.md](../README.md) for architecture overview
