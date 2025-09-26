# lib/book.py

class Book:
    """A Book class with title and page_count, using property() for validation."""

    def __init__(self, title, page_count):
        self._title = None
        self._page_count = None

        self.title = title
        self.page_count = page_count

    # TITLE property
    def get_title(self):
        return self._title

    def set_title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("title must be a non-empty string")
        self._title = value.strip()

    title = property(get_title, set_title)

    # PAGE_COUNT property
    def get_page_count(self):
        return self._page_count

    def set_page_count(self, value):
        #  Print instead of raise if not an int
        if not isinstance(value, int):
            print("page_count must be an integer")
            return
        if value <= 0:
            raise ValueError("page_count must be greater than 0")
        self._page_count = value

    page_count = property(get_page_count, set_page_count)

    #  Add turn_page() method to match test expectations
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def __repr__(self):
        return f"<Book title={self.title!r} page_count={self.page_count}>"