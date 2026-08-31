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

# Always validate: changed posts PLUS any draft:false post dated today.
# Future leftovers go live on their date even when this commit did not touch them.
CHANGED=""
if git rev-parse HEAD~1 >/dev/null 2>&1; then
  CHANGED=$(git diff --name-only HEAD~1 HEAD -- content/posts/ \
    | sed 's|.*/||;s|\.md$||' | grep -v '^_index$' || true)
fi
echo "Validating changed + going-live posts: ${CHANGED:-<none extra>}"
python3 scripts/validate_ncr_post.py --deploy-gate $CHANGED

# Download correct Hugo version
curl -sL https://github.com/gohugoio/hugo/releases/download/v0.147.1/hugo_extended_0.147.1_linux-amd64.tar.gz -o hugo.tar.gz
tar xzf hugo.tar.gz
chmod +x hugo

# Build
./hugo

echo "Build complete!"
