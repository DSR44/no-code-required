#!/bin/bash
set -e

# Download correct Hugo version
wget -q https://github.com/gohugoio/hugo/releases/download/v0.147.1/hugo_extended_0.147.1_linux-amd64.tar.gz
tar xzf hugo_extended_0.147.1_linux-amd64.tar.gz
chmod +x hugo

# Build
./hugo --minify

echo "Build complete!"
