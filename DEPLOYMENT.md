# Deployment Guide

This guide covers deploying CHAMP-LM in various environments.

## Table of Contents
1. [Local Development](#local-development)
2. [Docker Deployment](#docker-deployment)
3. [Production Setup](#production-setup)
4. [Environment Configuration](#environment-configuration)
5. [Monitoring & Logs](#monitoring--logs)
6. [Troubleshooting](#troubleshooting)

## Local Development

### Prerequisites
- Python 3.10+
- pip/virtualenv
- Make (optional but recommended)

### Quick Start

```bash
# Clone repository
git clone https://github.com/overandor/champ-lm.git
cd champ-lm

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Copy environment template
cp .env.example .env

# Run tests
pytest

# Start dashboard
streamlit run src/api/dashboard.py
```

The dashboard will be available at `http://localhost:8501`

## Docker Deployment

### Quick Deployment

```bash
# Build and start all services
docker-compose up --build

# Access dashboard at http://localhost:8501
# Metrics at http://localhost:9090
```

### Services

The Docker Compose setup includes:
- **champ-lm**: Main application with Streamlit dashboard
- **llama3-8b**: Ollama-based 8B parameter model
- **mistral-7b**: Ollama-based 7B parameter model

### Custom Configuration

Edit `docker-compose.yml`:

```yaml
services:
  champ-lm:
    environment:
      - SYMBOL=btcusdt       # Trading symbol
      - BATCH_SEC=30         # Batch interval
      - DATA_ROOT=/data      # Data directory
      # Add more env vars as needed
```

Or use `.env` file:
```bash
cp .env.example .env
# Edit .env with your values
docker-compose up --build
```

### Resource Limits

For production, adjust resource limits in `docker-compose.yml`:

```yaml
deploy:
  resources:
    limits:
      memory: 16G
      cpus: '4.0'
    reservations:
      memory: 8G
      cpus: '2.0'
```

## Production Setup

### System Requirements

- **CPU**: 4+ cores recommended
- **Memory**: 16GB minimum (32GB recommended with local models)
- **Storage**: 100GB+ for data and models
- **Network**: Stable internet connection
- **OS**: Linux (Ubuntu 20.04+ recommended)

### Production Deployment Steps

1. **Prepare server**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y docker.io docker-compose git

# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker
```

2. **Clone and setup**
```bash
git clone https://github.com/overandor/champ-lm.git
cd champ-lm
```

3. **Configure environment**
```bash
cp .env.example .env
# Edit .env with production values
nano .env
```

4. **Deploy with docker-compose**
```bash
# Build production images
docker-compose -f docker-compose.yml build

# Start services
docker-compose up -d

# Verify services
docker-compose ps
docker-compose logs -f champ-lm
```

5. **Set up monitoring**
```bash
# Access Prometheus metrics
curl http://localhost:9090

# Health check
curl http://localhost:8501/healthz
```

6. **Set up SSL/TLS (with Nginx)**
```bash
sudo apt install -y nginx certbot python3-certbot-nginx

# Create Nginx config
sudo nano /etc/nginx/sites-available/champ-lm

# Configure SSL
sudo certbot --nginx -d yourdomain.com

# Restart Nginx
sudo systemctl restart nginx
```

### Nginx Configuration Example

```nginx
server {
    listen 443 ssl http2;
    server_name yourdomain.com;
    
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    
    location / {
        proxy_pass http://localhost:8501;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    location /metrics {
        proxy_pass http://localhost:9090;
    }
}

server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$server_name$request_uri;
}
```

## Environment Configuration

### Essential Variables

```bash
# Symbol for market data
SYMBOL=btcusdt

# Data storage
DATA_ROOT=/data
ARCHIVE_CAP=12000

# LLM Configuration
MAX_RETRIES=3
RETRY_BACKOFF=1.5

# Circuit breaker
CB_FAILURES=5
CB_TIMEOUT=60

# Research parameters
NOVELTY_THRESHOLD=0.7
SIGNIFICANCE_THRESHOLD=0.05

# Monitoring
METRICS_PORT=9090
HEALTH_CHECK_INTERVAL=30

# Alerts (optional)
ALERT_WEBHOOK=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```

### Model Endpoints

```bash
# Ollama models (default)
# llama3-8b: http://llama3-8b:8001/generate
# mistral-7b: http://mistral-7b:8002/generate

# Custom models
MODEL_ENDPOINTS=model1:http://host1:8001/generate,model2:http://host2:8002/generate
```

## Monitoring & Logs

### View Logs

```bash
# Docker logs
docker-compose logs -f champ-lm

# Specific service
docker-compose logs -f llama3-8b

# Host logs (if running on system)
tail -f /var/log/champ-lm/app.log
```

### Prometheus Metrics

Access metrics at `http://localhost:9090`

Key metrics:
- `model_calls_total` - Total model invocations
- `request_latency_seconds` - Request timing
- `active_streams` - Active connections
- `memory_usage_bytes` - Memory consumption
- `cpu_usage_percent` - CPU utilization

### Health Checks

```bash
# Dashboard health
curl http://localhost:8501/healthz

# Metrics endpoint
curl http://localhost:9090

# Full health report
curl http://localhost:8501/health
```

## Troubleshooting

### Common Issues

**Port already in use**
```bash
# Find process using port 8501
lsof -i :8501

# Kill process
kill -9 <PID>

# Or use different port
docker-compose -e STREAMLIT_PORT=8502 up
```

**Out of memory**
```bash
# Check memory usage
docker stats

# Reduce model size or increase container memory
# Edit docker-compose.yml resources section
```

**Models not loading**
```bash
# Pull models manually
docker exec llama3-8b ollama pull llama2

# Check model status
docker exec llama3-8b ollama list
```

**Network connectivity issues**
```bash
# Test connectivity
docker-compose exec champ-lm curl http://llama3-8b:8001/generate

# Check network
docker network inspect champ-lm_default
```

### Debug Mode

Enable debug logging:

```bash
# In .env
LOG_LEVEL=DEBUG

# Restart services
docker-compose restart champ-lm
```

### Data Persistence

Default data location: `/data`

Backup data:
```bash
docker-compose exec champ-lm scripts/backup_archives.sh /data /backups
docker cp champ-lm:/backups ./backups-local
```

## Scaling

### Horizontal Scaling

For multiple instances, use load balancing:

```yaml
# docker-compose.yml
services:
  champ-lm:
    deploy:
      replicas: 3
```

Then configure Nginx upstream:
```nginx
upstream champ_backend {
    server champ-lm-1:8501;
    server champ-lm-2:8501;
    server champ-lm-3:8501;
}
```

### Model Optimization

- Use quantized models for faster inference
- Implement caching for frequently accessed data
- Monitor and optimize batch sizes
- Profile performance bottlenecks

## Support

- 📚 [Documentation](./README.md)
- 🐛 [Report Issues](https://github.com/overandor/champ-lm/issues)
- 💬 [Discussions](https://github.com/overandor/champ-lm/discussions)
