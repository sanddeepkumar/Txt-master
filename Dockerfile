#FROM python:3.9.7-slim-buster
FROM python:3.10.8-slim-buster

WORKDIR /app
COPY . .
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    aria2 \
    wget \
    build-essential \
    cmake \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r master.txt
RUN wget -O Bento4-SDK.zip https://github.com/axiomatic-systems/Bento4/archive/refs/heads/master.zip && \
    unzip Bento4-SDK.zip && \
    cd Bento4-master && \
    mkdir build && cd build && \
    cmake .. && \
    make mp4decrypt && \
    cp mp4decrypt /usr/local/bin/ && \
    cd ../.. && \
    rm -rf Bento4-SDK.zip Bento4-master
CMD gunicorn app:app & python3 modules/main.py
