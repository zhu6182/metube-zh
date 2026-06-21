FROM ghcr.io/alexta69/metube:latest

USER root

COPY patch-metube-zh-build.py /tmp/patch-metube-zh-build.py

RUN python3 /tmp/patch-metube-zh-build.py && \
    rm /tmp/patch-metube-zh-build.py

USER 1000

EXPOSE 8081
