#!/bin/bash
# hugo-insert-image.sh
# Usage: hugo-insert-image.sh <current-file-path>
# Picks an image, copies it to the post's images/ folder, puts markdown in clipboard.

CURRENT_FILE="$1"

if [ -z "$CURRENT_FILE" ]; then
  echo "Usage: $0 <path-to-current-markdown-file>"
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
    // User cancelled
    ""
  }
EOF
)

if [ -z "$IMAGE_PATH" ]; then
  echo "No image selected, exiting."
  exit 0
fi

# Get just the filename
IMAGE_FILENAME=$(basename "$IMAGE_PATH")

# Create images/ dir inside the post bundle
IMAGES_DIR="$POST_DIR/images"
mkdir -p "$IMAGES_DIR"

# Copy image there
cp "$IMAGE_PATH" "$IMAGES_DIR/$IMAGE_FILENAME"

# Build markdown snippet and copy to clipboard
MARKDOWN="![](images/$IMAGE_FILENAME)"
echo -n "$MARKDOWN" | pbcopy

echo "✓ Copied to $IMAGES_DIR/$IMAGE_FILENAME"
echo "✓ Clipboard: $MARKDOWN"
echo "  Just Cmd+V to paste into your markdown."
