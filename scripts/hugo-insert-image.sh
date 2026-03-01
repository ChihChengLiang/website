#!/bin/bash
# hugo-insert-image.sh
# Usage: hugo-insert-image.sh <current-file-path>
# Picks an image, converts to WebP, copies it to the post's images/ folder, puts markdown in clipboard.

CURRENT_FILE="$1"

if [ -z "$CURRENT_FILE" ]; then
  echo "Usage: $0 <path-to-current-markdown-file>"
  exit 1
fi

# Check cwebp is available
if ! command -v cwebp &> /dev/null; then
  osascript -e 'display alert "cwebp not found" message "Run: brew install webp"'
  exit 1
fi

# Derive the post folder (leaf bundle directory)
POST_DIR=$(dirname "$CURRENT_FILE")

# Pick image via JXA file picker
IMAGE_PATH=$(osascript -l JavaScript <<'EOF'
  var app = Application.currentApplication()
  app.includeStandardAdditions = true
  try {
    var image = app.chooseFile({
      withPrompt: "Select an image to insert:",
      ofType: ["public.image"]
    })
    image.toString()
  } catch(e) {
    ""
  }
EOF
)

if [ -z "$IMAGE_PATH" ]; then
  echo "No image selected, exiting."
  exit 0
fi

# Get filename without extension
IMAGE_FILENAME=$(basename "$IMAGE_PATH")
IMAGE_BASENAME="${IMAGE_FILENAME%.*}"

# Create images/ dir inside the post bundle
IMAGES_DIR="$POST_DIR/images"
mkdir -p "$IMAGES_DIR"

DEST="$IMAGES_DIR/${IMAGE_BASENAME}.webp"

# Convert to WebP at quality 80
cwebp -q 80 "$IMAGE_PATH" -o "$DEST" 2>/dev/null

if [ $? -ne 0 ]; then
  echo "✗ Conversion failed."
  exit 1
fi

# Show size comparison
ORIG_SIZE=$(du -sh "$IMAGE_PATH" | cut -f1)
NEW_SIZE=$(du -sh "$DEST" | cut -f1)

# Build markdown snippet and copy to clipboard
MARKDOWN="![](images/${IMAGE_BASENAME}.webp)"
echo -n "$MARKDOWN" | pbcopy

echo "✓ Converted: $ORIG_SIZE → $NEW_SIZE (WebP q80)"
echo "✓ Saved to: $DEST"
echo "✓ Clipboard: $MARKDOWN"
echo "  Just Cmd+V to paste into your markdown."
