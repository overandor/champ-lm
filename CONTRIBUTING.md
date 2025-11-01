# Contributing to CHAMP-LM

Thank you for your interest in contributing to CHAMP-LM! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please read our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) to understand our community standards.

## Getting Started

### Prerequisites
- Python 3.10+
- Docker & Docker Compose (for local testing)
- Git

### Development Setup

1. **Fork and clone the repository**
```bash
git clone https://github.com/yourusername/champ-lm.git
cd champ-lm
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -e ".[dev]"
```

4. **Set up pre-commit hooks**
```bash
pip install pre-commit
pre-commit install
```

## Development Workflow

### Creating a Branch

```bash
# Create a feature branch
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b fix/issue-description
```

**Branch naming conventions:**
- `feature/` - New features
- `fix/` - Bug fixes
- `refactor/` - Code refactoring
- `docs/` - Documentation updates
- `test/` - Test additions

### Code Style

We follow PEP 8 with these tools:
- **Black** for formatting
- **isort** for import ordering
- **flake8** for linting
- **mypy** for type checking

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Check linting
flake8 src/ tests/

# Check types
mypy src/
```

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_novelty.py

# Run async tests
pytest -m asyncio
```

### Writing Tests

- Place tests in the `tests/` directory
- Follow naming convention: `test_*.py`
- Use descriptive test names: `test_feature_description`
- Add async tests with `@pytest.mark.asyncio`

Example:
```python
def test_novelty_engine_scores_text() -> None:
    engine = NoveltyEngine()
    result = engine.score("Sample text with detailed content." * 5)
    assert 0.0 <= result.score <= 1.0
    assert result.rationale
```

## Making Changes

### Commit Messages

Follow conventional commits format:

```
type(scope): subject

body (optional)

footer (optional)
```

**Types:**
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation
- `style` - Code style changes
- `refactor` - Code refactoring
- `perf` - Performance improvements
- `test` - Test additions
- `chore` - Build, dependency updates

**Examples:**
```
feat(orchestrator): add retry logic for model clients
fix(stream): resolve websocket connection timeout
docs(readme): add installation instructions
test(research): add verification tests for GDP analyzer
```

## Submitting Changes

### Before Submitting

1. **Update tests** if needed
2. **Run full test suite**
   ```bash
   pytest --cov=src
   ```
3. **Format code**
   ```bash
   black src/ tests/
   isort src/ tests/
   ```
4. **Check types**
   ```bash
   mypy src/
   ```

### Pull Request Process

1. **Push to your fork**
```bash
git push origin feature/your-feature-name
```

2. **Open a Pull Request**
   - Use the PR template
   - Reference related issues: "Closes #123"
   - Provide clear description of changes
   - Add screenshots if applicable

3. **Respond to feedback**
   - Discuss changes constructively
   - Update PR if requested
   - Rebase on main if needed

4. **Merge**
   - Maintainers will merge after approval
   - Your contribution is now part of CHAMP-LM!

## Architecture Notes

### Key Components

- **`src/llm/`** - LLM orchestration and model clients
- **`src/metrics/`** - KPI engines and scoring
- **`src/streams/`** - Data stream management
- **`src/storage/`** - Data persistence
- **`src/monitoring/`** - Health checks and alerts
- **`contracts/`** - Solidity smart contracts

### Design Principles

- **Modularity**: Loosely coupled, independently testable components
- **Resilience**: Circuit breakers, retry logic, health checks
- **Observability**: Prometheus metrics, structured logging
- **Type Safety**: Type hints throughout

## Documentation

- Update [README.md](README.md) for user-facing changes
- Add docstrings to functions and classes
- Update [docs/](docs/) for architecture changes
- Reference existing documentation in commits

## Reporting Issues

Use GitHub Issues with:

1. **Clear title** describing the problem
2. **Steps to reproduce** the issue
3. **Expected behavior** vs actual behavior
4. **Environment details** (Python version, OS, etc.)
5. **Screenshots/logs** if applicable

## License

By contributing, you agree your code will be licensed under the MIT License.

## Questions?

- Check [README.md](README.md) and [docs/](docs/)
- Search existing issues
- Create a new discussion
- Open an issue tagged `question`

Thank you for contributing to CHAMP-LM! 🚀
