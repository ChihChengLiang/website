#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "requests>=2.31.0",
#     "pyperclip>=1.8.2",
#     "inquirer>=3.1.3",
# ]
# ///
"""
Book Search CLI Tool
Searches Google Books API and outputs markdown formatted book information.
"""

import sys
import argparse
import requests
import pyperclip
import inquirer

# Customizable Markdown Template
MARKDOWN_TEMPLATE = """## {title}

![Cover]({image_url})

**Author**: {authors}  
**Publisher**: {publisher}  
**Published**: {published_date}  
**ISBN-13**: {isbn13}
[View on Google Books]({link})
"""

def search_books(query):
    """Search Google Books API for books matching the query."""
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        'q': query,
        'maxResults': 10,
        'printType': 'books'
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if 'items' not in data:
            print(f"No results found for: {query}")
            sys.exit(1)
        
        return data['items']
    except requests.exceptions.RequestException as e:
        print(f"Error: API request failed - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def format_book_info(book):
    """Extract and format book information from API response."""
    volume_info = book.get('volumeInfo', {})
    
    # Extract basic information
    title = volume_info.get('title', 'N/A')
    authors = ', '.join(volume_info.get('authors', ['N/A']))
    publisher = volume_info.get('publisher', 'N/A')
    published_date = volume_info.get('publishedDate', 'N/A')
    link = volume_info.get('canonicalVolumeLink', 'N/A')
    
    # Get largest available cover image
    image_links = volume_info.get('imageLinks', {})
    image_url = (
        image_links.get('extraLarge') or
        image_links.get('large') or
        image_links.get('medium') or
        image_links.get('small') or
        image_links.get('thumbnail') or
        'No image available'
    )
    
    # Extract ISBNs
    isbn13 = 'N/A'
    
    for identifier in volume_info.get('industryIdentifiers', []):
        if identifier['type'] == 'ISBN_13':
            isbn13 = identifier['identifier']

    return {
        'title': title,
        'authors': authors,
        'publisher': publisher,
        'published_date': published_date,
        'link': link,
        'image_url': image_url,
        'isbn13': isbn13,
    }

def select_book(books):
    """Interactive book selection using arrow keys."""
    choices = []
    for book in books:
        volume_info = book.get('volumeInfo', {})
        title = volume_info.get('title', 'Unknown Title')
        authors = ', '.join(volume_info.get('authors', ['Unknown Author']))
        published_date = volume_info.get('publishedDate', 'N/A')
        
        display = f"{title} - {authors} ({published_date})"
        choices.append((display, book))
    
    questions = [
        inquirer.List('book',
                     message="Select a book",
                     choices=[(display, book) for display, book in choices],
                     carousel=True)
    ]
    
    answers = inquirer.prompt(questions)
    
    if answers is None:
        print("\nSelection cancelled.")
        sys.exit(0)
    
    return answers['book']

def generate_markdown(book):
    """Generate markdown output for the selected book."""
    book_info = format_book_info(book)
    markdown = MARKDOWN_TEMPLATE.format(**book_info)
    return markdown

def main():
    parser = argparse.ArgumentParser(
        description='Search Google Books API and output markdown formatted book information.'
    )
    parser.add_argument('query', help='Search query string')
    parser.add_argument('-c', '--clipboard', action='store_true',
                       help='Copy output to clipboard instead of stdout')
    
    args = parser.parse_args()
    
    # Search for books
    print(f"Searching for: {args.query}")
    books = search_books(args.query)
    print(f"Found {len(books)} results.\n")
    
    # Interactive selection
    selected_book = select_book(books)
    
    # Generate markdown
    markdown = generate_markdown(selected_book)
    
    # Output
    if args.clipboard:
        pyperclip.copy(markdown)
        print("\n✓ Markdown copied to clipboard!")
    else:
        print("\n" + "="*80)
        print(markdown)
        print("="*80)

if __name__ == '__main__':
    main()
