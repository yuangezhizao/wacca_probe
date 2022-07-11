# https://docs.pylonsproject.org/projects/waitress/en/stable/usage.html#heroku

# web: waitress-serve --host=0.0.0.0 --port=$PORT --threads=4 --backlog=1024 --asyncore-use-poll --trusted-proxy '*' --trusted-proxy-headers 'x-forwarded-for x-forwarded-proto x-forwarded-port' --log-untrusted-proxy-headers --clear-untrusted-proxy-headers --call src.wacca_probe:create_app

web: gunicorn --workers 1 --threads 1 --bind 0.0.0.0:$PORT --pythonpath ./src "wacca_probe:create_app()" --log-level debug --access-logfile - --error-logfile - --max-requests 10000 --timeout 5 --keep-alive 5
