# Topic 11: Writing Maintainable and Production-Ready Python

You have reached the final topic! We have covered data structures, classes, decorators, errors, and async. Now, we need to talk about how a professional engineer organizes a **whole project**.

In a real backend (like a **FastAPI** project), we use a pattern called **Separation of Concerns**. We don't put everything in one file.

### 1. The Standard Project Structure
A professional Python project usually looks like this:

```text
my_project/
├── venv/                 # Virtual environment
├── requirements.txt      # List of packages
├── .gitignore            # Files to hide from GitHub
├── main.py               # The "Entry Point" (Starts the app)
└── app/
    ├── __init__.py       # Makes 'app' a package
    ├── models.py         # Database Classes (User, Product)
    ├── services.py       # Business Logic (Logic for login, payments)
    └── utils.py          # Helper functions (Formatters, Loggers)
```

### 2. The `__init__.py` file
When you see this file in a folder, it tells Python: *"This folder is a package."* This allows you to do `from app.services import login_user`.

### 3. Clean Code (The "Zen of Python")
As a senior dev, I look for three things in your code:
*   **Type Hints:** Are they present?
*   **Docstrings:** Do you explain what the function does?
*   **Naming:** Do your variables make sense? (`u` is bad; `current_user` is good).

---

### The Final "Grand Capstone" Challenge

You are building a tiny **Library System**. You need to create a modular structure.

**Task:**
1.  Create a class `Book` in your mind (Attributes: `title`, `author`).
2.  Create a class `Library`. It should have a list called `books`.
3.  Add a method `add_book(self, book: Book)`.
4.  Add an `async` method `search_catalog(self, query: str)`. 
    *   It should `await asyncio.sleep(0.5)` (simulating a database search).
    *   Use a **List Comprehension** to return all books where the query is in the title.
5.  Wrap everything in a `try...except` block in the `main()` function to handle any errors.

**Starter Structure:**

```python
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
        # TODO: Implement async search with list comprehension
        pass

async def main():
    # TODO: Create library, add 2 books, and await a search
    # TODO: Use try/except and logging
    pass

if __name__ == "__main__":
    asyncio.run(main())
```

**This is your final exam.** Combine everything: Classes, Type Hints, Async, List Comprehensions, and Error Handling.

**Show me what you've learned!**
**Answer Found in 17finalpro.py**