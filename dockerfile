FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    make \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN make html

EXPOSE 8000
CMD ["python", "-m", "http.server", "8000", "--directory", "_build/html"]