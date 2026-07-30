# CHAMP-LM — operating modes

Research orchestration engine (LLM ensembles + novelty/impact KPIs + resilient
streaming). Part of the
[syndication standard](https://github.com/overandor/jorki/blob/main/syndication/STANDARD.md).

| Mode | Command | Requires | Status |
|---|---|---|---|
| `dev` | `pip install -e ".[dev]"` then `streamlit run src/api/dashboard.py` | Python 3.10+, `.env` config, LLM provider keys, internet | dashboard at `http://localhost:8501` |
| `docker` | `docker-compose up --build` | Docker, `.env` | full stack (dashboard + services) |
| `test` | `pytest` | dev extras | CI: “Tests & Quality” workflow |

## Configuration

```bash
cp .env.example .env   # then set LLM provider keys and stream/config values
```

## Honest notes

- Requires **external LLM provider credentials** and network access; there is no
  fully offline mode.
- `src/streams/` includes market-data ingestion (`binance_stream.py`,
  `solana_stream.py`). These are **data sources for research KPIs**, not a
  trading/execution engine — CHAMP-LM orchestrates LLM research rounds, it does
  not place orders.
