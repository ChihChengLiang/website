# Book Search CLI Tool

A command-line tool that searches the Google Books API and outputs book information in markdown format

## Installation

```bash
chmod +x book_search.py
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
- `{image_url}` - Cover image URL (largest available)
- `{link}` - Canonical Google Books link

## License

Free to use and modify for your blog and personal projects.
