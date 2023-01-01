FROM python:3.11-slim-bullseye AS build-venv

WORKDIR /app

COPY requirements.txt .

#RUN python3.11 -m venv venv && \
#    venv/bin/pip3.11 install --upgrade pip setuptools wheel && \
#    venv/bin/pip3.11 install --disable-pip-version-check --no-cache-dir gunicorn[gevent] && \
#    venv/bin/pip3.11 install --disable-pip-version-check --no-cache-dir -r requirements.txt
RUN pip3.11 install --upgrade pip setuptools wheel && \
    pip3.11 install --disable-pip-version-check --no-warn-script-location --no-cache-dir --user gunicorn[gevent] &&  \
    pip3.11 install --disable-pip-version-check --no-warn-script-location --no-cache-dir --user -r requirements.txt

#FROM gcr.io/distroless/python3-debian11:debug
#FROM python:3.11-alpine
FROM python:3.11-slim-bullseye

LABEL maintainer="yuangezhizao <root@yuangezhizao.cn>"

#COPY --from=build-venv /app/venv /app/venv
COPY --from=build-venv /root/.local /root/.local

WORKDIR /app

COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#ENV PATH=/app/venv/bin:$PATH
ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000

HEALTHCHECK --timeout=10s --interval=30s --retries=3 CMD curl http://localhost:5000 || exit 1

CMD ["gunicorn", "--worker-class", "gevent", "--workers", "8", "--bind", "0.0.0.0:5000", "--pythonpath", "/app/src", "wacca_probe:create_app()", "--max-requests", "10000", "--timeout", "5", "--keep-alive", "5", "--log-level", "info"]
