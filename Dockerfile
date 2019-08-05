FROM python:latest
WORKDIR /app

RUN apt update && \
    apt install -y dnsutils inetutils-ping && \
    pip install fastapi[all] dnspython

COPY ./src .

# Flask default port
EXPOSE 5000
ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
