#!/bin/bash
set -e

# Install system dependencies required for dlib
apt-get update
apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev
