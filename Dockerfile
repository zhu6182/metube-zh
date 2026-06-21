FROM ghcr.io/alexta69/metube:latest

USER root

COPY patch-metube-zh-build.py /tmp/patch-metube-zh-build.py

RUN python3 /tmp/patch-metube-zh-build.py && \
    rm /tmp/patch-metube-zh-build.py && \
    mkdir -p /tmp/downloads && \
    chown -R 1000:1000 /tmp/downloads

ENV DOWNLOAD_DIR=/tmp/downloads \
    STATE_DIR=/tmp/downloads/.metube \
    TEMP_DIR=/tmp/downloads \
    AUDIO_DOWNLOAD_DIR=/tmp/downloads

USER 1000

EXPOSE 8081
