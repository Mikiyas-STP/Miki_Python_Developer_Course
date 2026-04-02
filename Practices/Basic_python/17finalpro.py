import asyncio
import logging

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    async def search_catalog(self, query: str) -> list[Book]:
        await asyncio.sleep(0.5)
        # We search the TITLE of each book object
        return [b for b in self.books if query.lower() in b.title.lower()]

async def main():
    logging.basicConfig(level=logging.INFO)
    
    try:
        # Step 1: Initialize
        lib = Library()
        
        # Step 2: Create Data
        lib.add_book(Book("The Lion King", "Disney"))
        lib.add_book(Book("Python Backend Pro", "Mentor"))
        
        # Step 3: Action (Async)
        print("Searching...")
        results = await lib.search_catalog("Python")
        
        # Step 4: Display
        if results:
            for b in results:
                print(f"Match Found: {b.title}")
        else:
            print("No matches found.")

    except Exception as e:
        logging.error(f"App Crash: {e}")

if __name__ == "__main__":
    asyncio.run(main())