# Book Search CLI Tool

A command-line tool that searches the Google Books API and outputs book information in markdown format, perfect for blog posts and book reviews.

## Features

- 🔍 Search Google Books API
- ⌨️ Interactive book selection with arrow keys
- 📋 Copy to clipboard or output to stdout
- 📝 Customizable markdown template
- 🖼️ Automatically selects the largest available cover image
- 📚 Includes ISBN-13 (and ISBN-10 if available)
- ⚡ Uses `uv` - no Python environment management needed!

## Installation

### Option 1: Using uv (Recommended)

1. Install `uv` if you haven't already:
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip
pip install uv
```

2. Make the script executable:
```bash
chmod +x book_search.py
```

That's it! The script will automatically handle all dependencies when you run it.

### Option 2: Traditional Python (if you prefer)

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Using uv (no setup required):
```bash
# Just run it directly!
./book_search.py "The Great Gatsby"

# Or with python
uv run book_search.py "The Great Gatsby"
```

### Copy to clipboard:
```bash
./book_search.py "1984 George Orwell" --clipboard
# or
./book_search.py "1984 George Orwell" -c
```

### Traditional Python:
```bash
python book_search.py "The Great Gatsby"
```

### Interactive selection:
After running the command, use arrow keys to navigate through search results and press Enter to select.

## Customizing the Template

The markdown template is embedded in the script at the top. Simply edit the `MARKDOWN_TEMPLATE` variable in `book_search.py` to match your blog's format:

```python
MARKDOWN_TEMPLATE = """## {title}

![Cover]({image_url})

**Author**: {authors}  
**Publisher**: {publisher}  
**Published**: {published_date}  
...
"""
```

Available template variables:
- `{title}` - Book title
- `{authors}` - Comma-separated list of authors
- `{publisher}` - Publisher name
- `{published_date}` - Publication date
- `{isbn13}` - ISBN-13 number
- `{isbn10_line}` - ISBN-10 line (empty if not available)
- `{page_count}` - Number of pages
- `{categories}` - Book categories/genres
- `{description}` - Book description/summary
- `{image_url}` - Cover image URL (largest available)
- `{link}` - Canonical Google Books link

## Example Output

```markdown
## The Great Gatsby

![Cover](https://books.google.com/books/content?id=...)

**Author**: F. Scott Fitzgerald  
**Publisher**: Scribner  
**Published**: 2004-09-30  
**ISBN-13**: 9780743273565  
**ISBN-10**: 0743273565  
**Pages**: 180  
**Categories**: Fiction

The Great Gatsby, F. Scott Fitzgerald's third book...

[View on Google Books](https://books.google.com/books?id=...)
```

## Requirements

### For uv (Recommended):
- `uv` installed ([installation instructions](https://github.com/astral-sh/uv))
- Internet connection (for API access)
- That's it! All Python dependencies are handled automatically

### For traditional Python:
- Python 3.8+
- Internet connection (for API access)
- Dependencies listed in requirements.txt

## Troubleshooting

- **No results found**: Try a more specific or different query
- **Clipboard not working**: Make sure `pyperclip` is installed correctly
- **API errors**: Check your internet connection

## License

Free to use and modify for your blog and personal projects.
