# CHAMP-LM: Research Orchestration Engine

[![Tests & Quality](https://github.com/overandor/champ-lm/workflows/Tests%20&%20Quality/badge.svg)](https://github.com/overandor/champ-lm/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**CHAMP-LM** is a modular research orchestration engine for running continuous novelty discovery rounds with large language model ensembles. It combines streaming data ingestion, LLM orchestration, KPI tracking, and resilient monitoring into a production-ready platform.

## 🎯 Key Features

- **🤖 LLM Ensemble Orchestration**: Coordinate multiple LLM providers with intelligent retry logic and circuit breakers
- **📊 Research KPI Engines**: Track novelty, impact, and publication readiness metrics
- **🔄 Resilient Streaming**: WebSocket connections with automatic reconnection and health monitoring
- **📈 Real-time Metrics**: Prometheus-based observability with custom research KPIs
- **⛓️ Blockchain Integration**: Solidity smart contracts for KPI token management
- **🔐 Audit Trail**: Merkle logger for cryptographic verification of research records
- **🐳 Docker Ready**: Complete containerization with compose setup
- **🧪 Well-Tested**: Comprehensive test suite with CI/CD pipelines

## 🚀 Quick Start

### Prerequisites
- Python 3.10+ or Docker
- 4GB+ RAM (16GB+ recommended)
- Internet connection

### Installation

**Option 1: Local Development**
```bash
git clone https://github.com/overandor/champ-lm.git
cd champ-lm
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

**Option 2: Docker**
```bash
git clone https://github.com/overandor/champ-lm.git
cd champ-lm
docker-compose up --build
```

### Configuration

```bash
cp .env.example .env
# Edit .env with your configuration
```

### Run

**Local:**
```bash
streamlit run src/api/dashboard.py
```

**Docker:**
```bash
docker-compose up
```

Access the dashboard at `http://localhost:8501`

## 📋 Architecture

### Core Components

```
src/
├── llm/              # LLM orchestration and clients
│   ├── orchestrator.py
│   └── model_client.py
├── metrics/          # KPI engines and scoring
│   ├── novelty_engine.py
│   ├── impact_engine.py
│   └── research_kpis.py
├── streams/          # Data stream management
│   ├── stream_manager.py
│   ├── binance_stream.py
│   └── solana_stream.py
├── storage/          # Data persistence
│   ├── merkle_logger.py
│   └── archive_manager.py
├── monitoring/       # Health and alerts
│   ├── health.py
│   ├── alerts.py
│   └── metrics.py
└── kpi_engine/       # Economic KPIs
    ├── econometrics.py
    └── economic_singularity.py
```

### Architecture Diagram

```
┌─────────────────────────────────────────┐
│     Data Streams (Binance, Solana)      │
└──────────────────┬──────────────────────┘
                   │
        ┌──────────▼──────────┐
        │  Stream Manager     │
        │ (Circuit Breakers)  │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────────────┐
        │  LLM Orchestrator           │
        │ (Parallel Execution)        │
        └──────────┬──────────────────┘
                   │
        ┌──────────▼──────────────────┐
        │  Research KPI Engine        │
        │ (Novelty, Impact, Pub Ready)│
        └──────────┬──────────────────┘
                   │
        ┌──────────▼──────────────────┐
        │  Merkle Logger              │
        │ (Audit Trail)               │
        └──────────┬──────────────────┘
                   │
        ┌──────────▼──────────────────┐
        │  Prometheus Metrics         │
        │  Health Monitor             │
        └─────────────────────────────┘
```

## 📚 Documentation

- [Installation & Setup](./docs/setup.md)
- [Deployment Guide](./DEPLOYMENT.md)
- [Contributing Guidelines](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [API Reference](./docs/api.md)
- [Architecture Design](./docs/dual_force_liquidity_ecology.md)

## 🧪 Testing

```bash
# Run all tests
pytest

# With coverage
pytest --cov=src --cov-report=html

# Specific test file
pytest tests/test_novelty.py -v

# Async tests
pytest -m asyncio
```

## 🔧 Configuration

### Environment Variables

```bash
# Market symbol
SYMBOL=btcusdt

# Data storage
DATA_ROOT=/data
ARCHIVE_CAP=12000

# LLM retry logic
MAX_RETRIES=3
RETRY_BACKOFF=1.5

# Circuit breaker
CB_FAILURES=5
CB_TIMEOUT=60

# Research thresholds
NOVELTY_THRESHOLD=0.7
SIGNIFICANCE_THRESHOLD=0.05

# Monitoring
METRICS_PORT=9090
HEALTH_CHECK_INTERVAL=30

# Alerts (optional)
ALERT_WEBHOOK=https://hooks.slack.com/services/YOUR/WEBHOOK
```

See [.env.example](.env.example) for complete configuration.

## 📊 Monitoring

### Prometheus Metrics

Access metrics at `http://localhost:9090`

Key metrics:
- `model_calls_total` - Total LLM invocations
- `request_latency_seconds` - Request response times
- `active_streams` - Active connections
- `memory_usage_bytes` - Memory consumption
- `cpu_usage_percent` - CPU utilization

### Health Endpoint

```bash
curl http://localhost:8501/healthz
curl http://localhost:8501/health  # Detailed health report
```

## 🏗️ Project Structure

```
champ-lm/
├── src/                 # Source code
├── tests/               # Test suite
├── contracts/           # Solidity smart contracts
├── config/              # Configuration files
├── scripts/             # Utility scripts
├── data/                # Sample data
├── docs/                # Documentation
├── .github/             # GitHub templates and workflows
├── docker-compose.yml   # Docker Compose setup
├── Dockerfile           # Container image
├── pyproject.toml       # Python project config
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## 🔗 Smart Contracts

Solidity contracts for KPI token management:

```solidity
// KPIRegistry - Manages KPI tokens
// PromptNFT - Tracks prompt evaluations  
// AppraisalRouter - Routes rewards
// CompositeIndex - Weighted KPI index
```

See [contracts/KPIFactory.sol](contracts/KPIFactory.sol)

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Development setup
- Code style guidelines
- Testing requirements
- Pull request process
- Commit conventions

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for release history and upcoming features.

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 🆘 Support & Community

- 📚 [Read the Docs](./docs/)
- 🐛 [Report Issues](https://github.com/overandor/champ-lm/issues)
- 💬 [Discussions](https://github.com/overandor/champ-lm/discussions)
- 📧 Create an issue for questions

## 👥 Authors

- **overandor** - Initial author

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io) for the dashboard
- LLM orchestration powered by [aiohttp](https://aiohttp.readthedocs.io)
- Metrics with [Prometheus](https://prometheus.io)
- Contracts in [Solidity](https://soliditylang.org)

## 🔮 Roadmap

- [ ] Enhanced UI improvements
- [ ] Additional LLM provider support (OpenAI, Anthropic, etc.)
- [ ] Advanced analytics dashboards
- [ ] Distributed deployment support
- [ ] GraphQL API
- [ ] Extended test coverage (90%+)
- [ ] Performance optimizations

## ⚡ Quick Commands

```bash
# Setup
git clone https://github.com/overandor/champ-lm.git
cd champ-lm
python -m venv venv && source venv/bin/activate
pip install -e ".[dev]"

# Development
pre-commit install
black src tests && isort src tests && flake8 src tests
pytest --cov=src

# Docker
docker-compose up --build
docker-compose logs -f

# Deployment
# See DEPLOYMENT.md for detailed instructions
```

---

**Made with ❤️ for the research community**
