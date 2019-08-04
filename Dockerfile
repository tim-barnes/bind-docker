FROM ubuntu:18.10

RUN apt update && \
    apt install -y dnsutils inetutils-ping
