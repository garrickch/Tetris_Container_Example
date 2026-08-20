# Example Production Dockerfile (Example, not meant to be used)


FROM python:3.12-slim AS builder

WORKDIR /code

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.12-slim AS runner

WORKDIR /code

RUN useradd -u 8888 appuser && chown -R appuser:appuser /code
USER appuser

COPY --from=builder --chown=appuser:appuser /root/.local /home/appuser/.local
ENV PATH=/home/appuser/.local/bin:$PATH

COPY --chown=appuser:appuser src/ ./src/
COPY --chown=appuser:appuser data/ ./data/

ENV PYTHONPATH=/code/src
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["python", "-m", "src.project.main"]
