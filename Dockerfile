FROM python:3.10.5-bullseye

LABEL maintainer="yuangezhizao <root@yuangezhizao.cn>"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./

RUN pip3.10 install -i https://mirrors.cloud.tencent.com/pypi/simple --upgrade pip setuptools wheel && \
    pip3.10 config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple && \
    pip3.10 install --disable-pip-version-check --no-cache-dir gunicorn[gevent] && \
    pip3.10 install --disable-pip-version-check --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

HEALTHCHECK --timeout=10s --interval=30s --retries=3 CMD curl http://localhost:5000 || exit 1

CMD ["gunicorn", "--worker-class", "gevent", "--workers", "8", "--bind", "0.0.0.0:5000", "--pythonpath", "/app/src", "wacca_probe:create_app()", "--max-requests", "10000", "--timeout", "5", "--keep-alive", "5", "--log-level", "info"]
