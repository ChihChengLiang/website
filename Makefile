DATE := $(shell date +%Y-%m-%d)

.PHONY: new new-zh serve

new:
	@read -p "Slug (e.g. lean_lang): " slug; \
	hugo new content/posts/$(DATE)_$${slug}/index.md; \

new-zh:
	@read -p "Slug (e.g. lean_lang): " slug; \
	hugo new content/posts/$(DATE)_$${slug}/index.zh-TW.md; \

serve:
	hugo server -D --navigateToChanged

book:
	@read -p "Book title to search: " title; \
	uv run book_search/book_search.py -c "$${title}"; \

s: serve
