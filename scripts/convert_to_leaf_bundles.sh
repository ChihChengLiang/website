#!/bin/bash

# Script to convert Hugo posts to leaf bundles
# Each post becomes a directory with index.md (or index.LANG.md for translations)

set -e

POSTS_DIR="content/posts"

cd "$(dirname "$0")/.."

echo "Converting posts to leaf bundles..."

# Process all .md files in the posts directory
for file in "$POSTS_DIR"/*.md; do
    [ -f "$file" ] || continue

    filename=$(basename "$file")

    # Skip if not a markdown file
    [[ "$filename" != *.md ]] && continue

    # Check if this is a language variant (e.g., file.zh-TW.md)
    if [[ "$filename" =~ ^(.+)\.([a-z]{2}(-[A-Z]{2})?)\.md$ ]]; then
        # Language variant
        base_name="${BASH_REMATCH[1]}"
        lang="${BASH_REMATCH[2]}"
        target_dir="$POSTS_DIR/$base_name"
        target_file="index.$lang.md"
    else
        # Default language file
        base_name="${filename%.md}"
        target_dir="$POSTS_DIR/$base_name"
        target_file="index.md"
    fi

    # Create directory if it doesn't exist
    if [ ! -d "$target_dir" ]; then
        echo "Creating directory: $target_dir"
        mkdir -p "$target_dir"
    fi

    # Move the file
    echo "Moving $filename -> $target_dir/$target_file"
    mv "$file" "$target_dir/$target_file"
done

echo ""
echo "Conversion complete!"
echo ""
echo "Summary of leaf bundles created:"
for dir in "$POSTS_DIR"/*/; do
    [ -d "$dir" ] || continue
    echo "  $(basename "$dir")/"
    ls -1 "$dir" | sed 's/^/    /'
done
