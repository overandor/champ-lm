# CHAMP-LM — importable components

CHAMP-LM is an application (Streamlit dashboard + services), not a published pip
package. Its “SDK” surface is the installable `src/` package you can import after
`pip install -e ".[dev]"`. Part of the
[syndication standard](https://github.com/overandor/jorki/blob/main/syndication/STANDARD.md).

## Install

```bash
pip install -e ".[dev]"
```

## Component map

| Module | Purpose |
|---|---|
| `src/llm/orchestrator.py` | Coordinate multiple LLM providers (retry, circuit breakers) |
| `src/llm/model_client.py` | Provider client abstraction |
| `src/metrics/novelty_engine.py` | Novelty scoring |
| `src/metrics/impact_engine.py` | Impact scoring |
| `src/metrics/research_kpis.py` | Research KPI definitions |
| `src/streams/stream_manager.py` | Streaming data ingestion + health |
| `src/storage/merkle_logger.py` | Merkle-logged, cryptographically verifiable audit trail |
| `src/storage/archive_manager.py` | Persistence / archival |
| `src/monitoring/{health,alerts,metrics}.py` | Observability (Prometheus) |
| `src/api/dashboard.py` | Streamlit entrypoint |

## Stability

- Exact public symbols per module are not yet frozen — treat imports as
  **experimental** until the package pins its public API. Run `pytest` to see
  the exercised surface.
- The dashboard (`src/api/dashboard.py`) and Docker compose are the supported
  entrypoints (see [`MODES.md`](MODES.md)).
