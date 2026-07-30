# CHAMP-LM runtime image.
FROM python:3.11-slim

WORKDIR /app
COPY . .

# Runtime install (not the [dev] extras) — this image runs the app, not the tests.
RUN pip install --no-cache-dir . || pip install --no-cache-dir -e .

EXPOSE 8501
CMD ["streamlit", "run", "src/api/dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
