.PHONY: help install install-dev setup test lint format type-check clean docker-build docker-up docker-down docs

help:
	@echo "CHAMP-LM Development Commands"
	@echo "=============================="
	@echo ""
	@echo "Setup:"
	@echo "  make install        - Install production dependencies"
	@echo "  make install-dev    - Install all dependencies including dev tools"
	@echo "  make setup          - Setup development environment (venv + deps)"
	@echo ""
	@echo "Development:"
	@echo "  make lint           - Run linting checks (flake8, mypy)"
	@echo "  make format         - Format code (black, isort)"
	@echo "  make type-check     - Run type checking"
	@echo "  make test           - Run test suite"
	@echo "  make test-cov       - Run tests with coverage report"
	@echo "  make test-watch     - Run tests in watch mode"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build   - Build Docker images"
	@echo "  make docker-up      - Start docker-compose services"
	@echo "  make docker-down    - Stop docker-compose services"
	@echo "  make docker-logs    - View docker-compose logs"
	@echo ""
	@echo "Utility:"
	@echo "  make clean          - Clean build artifacts and cache"
	@echo "  make pre-commit     - Run pre-commit hooks"
	@echo "  make docs           - Build documentation"
	@echo ""

install:
	pip install -r requirements.txt

install-dev:
	pip install -e ".[dev]"

setup:
	python -m venv venv
	@echo "Virtual environment created. Run: source venv/bin/activate"
	$(MAKE) install-dev

test:
	pytest tests/ -v

test-cov:
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term-missing
	@echo "Coverage report generated: htmlcov/index.html"

test-watch:
	pytest-watch tests/

lint:
	flake8 src tests
	mypy src --ignore-missing-imports

format:
	black src tests
	isort src tests

type-check:
	mypy src --ignore-missing-imports

pre-commit:
	pre-commit run --all-files

docker-build:
	docker-compose build

docker-up:
	docker-compose up -d
	@echo "Services started. Dashboard: http://localhost:8501"

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f

docker-clean:
	docker-compose down -v
	docker system prune -f

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .mypy_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name htmlcov -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".coverage" -delete
	rm -rf build dist *.egg-info 2>/dev/null || true

run-local:
	streamlit run src/api/dashboard.py

run-tests-all:
	pytest tests/ -v --cov=src --cov-report=html

security:
	bandit -r src -f json -o bandit-report.json || true
	safety check || true

requirements-update:
	pip list --outdated

install-pre-commit:
	pip install pre-commit
	pre-commit install

version:
	@python -c "import src; print(src.__version__)" 2>/dev/null || echo "Version info not found"

.DEFAULT_GOAL := help
