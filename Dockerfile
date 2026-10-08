FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FASTEMBED_CACHE_DIR=/app/.cache/fastembed

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN addgroup --system --gid 10001 apolloai \
    && adduser --system --uid 10001 --ingroup apolloai --home /app --no-create-home apolloai \
    && mkdir -p /app/.cache/fastembed \
    && chown -R 10001:10001 /app/.cache
COPY --chown=apolloai:apolloai . .

USER 10001:10001

EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
    CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:5000/live', timeout=3)"]
CMD ["sh", "deploy/start.sh"]
