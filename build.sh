#!/bin/bash
set -e

# Initialize submodules (PaperMod theme)
git submodule update --init --recursive

# Block deploy if a changed post is missing cover image or audio (prevents markdown-only publishes)
if git rev-parse HEAD~1 >/dev/null 2>&1; then
  CHANGED=$(git diff --name-only HEAD~1 HEAD -- content/posts/ \
    | sed 's|.*/||;s|\.md$||' | grep -v '^_index$' || true)
  if [ -n "$CHANGED" ]; then
    echo "Validating changed posts: $CHANGED"
    # Deploy gate: only HARD failures (missing cover/audio) block the build.
    # Soft SEO issues (link count, word count) warn but never take the site down.
    python3 scripts/validate_ncr_post.py --deploy-gate $CHANGED
  fi
fi

# Download correct Hugo version
curl -sL https://github.com/gohugoio/hugo/releases/download/v0.147.1/hugo_extended_0.147.1_linux-amd64.tar.gz -o hugo.tar.gz
tar xzf hugo.tar.gz
chmod +x hugo

# Build
./hugo --minify

echo "Build complete!"
