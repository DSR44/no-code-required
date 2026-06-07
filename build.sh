#!/bin/bash
set -e

# Ensure PaperMod theme is present (submodule may not init on Vercel)
if [ ! -f themes/PaperMod/layouts/_default/baseof.html ]; then
  echo "PaperMod theme missing — downloading..."
  rm -rf themes/PaperMod
  curl -sL https://github.com/adityatelange/hugo-PaperMod/archive/refs/tags/v8.0.tar.gz | tar xz
  mv hugo-PaperMod-8.0 themes/PaperMod
  echo "PaperMod downloaded."
fi

# Block deploy if a changed post is missing cover image or audio (prevents markdown-only publishes)
if git rev-parse HEAD~1 >/dev/null 2>&1; then
  CHANGED=$(git diff --name-only HEAD~1 HEAD -- content/posts/ \
    | sed 's|.*/||;s|\.md$||' | grep -v '^_index$' || true)
  if [ -n "$CHANGED" ]; then
    echo "Validating changed posts: $CHANGED"
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
