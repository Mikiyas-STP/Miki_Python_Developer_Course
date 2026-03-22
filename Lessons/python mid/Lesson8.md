# Topic 8: Error Handling and Logging

In backend development, we stop using `print()` for everything. In production, no one sees the "console." We use **Logging** to write to files or cloud services (like AWS CloudWatch).

#### 1. The `logging` Library
Python has a built-in `logging` module with different levels:
*   `DEBUG`: Tiny details for devs.
*   `INFO`: General events (User logged in).
*   `WARNING`: Something unusual happened.
*   `ERROR`: Something broke (Database connection failed).
*   `CRITICAL`: The whole server is going down.

```python
import logging

# Basic configuration
logging.basicConfig(level=logging.INFO)

logging.info("Server started on port 8000")
logging.error("Failed to process payment for User #123")
```

#### 2. Specific Exception Handling
Never use a "bare" `except`. Always catch the specific error you expect.

**The Backend Example: Division API**
```python
def divide_funds(total: float, people: int):
    try:
        return total / people
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero!")
        return 0
    except TypeError:
        logging.error("Invalid input types provided.")
        return 0
```

---

### Real-World Backend Example: Data Loading

Imagine you are reading a configuration file for your API.

```python
import logging

def load_config(file_path: str):
    try:
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        logging.error(f"CRITICAL: Config file {file_path} is missing!")
        return "{}" # Return an empty JSON string as a fallback
```

---

### Your Coding Challenge: The "Safe API Client"

You are building a client that fetches data from an external API. Sometimes the API is down, and sometimes the data is corrupted.

**Task:**
1.  Create a function called `fetch_api_data`. It takes a `status_code: int`.
2.  **Logic:**
    *   If the code is `404`, **raise** a `FileNotFoundError`.
    *   If the code is `500`, **raise** a `ConnectionError`.
    *   Otherwise, return `"Data received!"`
3.  Create a second function called `process_request`.
    *   It should call `fetch_api_data`.
    *   Use a `try/except` block to catch **both** types of errors.
    *   If an error occurs, use `logging.error()` to log the specific message and return `None`.
    *   If it succeeds, return the data.

**Starter Code:**
```python
import logging

# Configure logging to show messages
logging.basicConfig(level=logging.INFO)

def fetch_api_data(status_code: int) -> str:
    # TODO: Raise exceptions based on status_code
    pass

def process_request(code: int):
    # TODO: Wrap fetch_api_data in try/except
    pass

# Test calls
print(process_request(200)) # Should return data
print(process_request(404)) # Should log error and return None
print(process_request(500)) # Should log error and return None
```

**Senior Hint:** You can catch multiple exceptions in one block using `except (ErrorA, ErrorB) as e:`.

**Show me how you handle these backend failures!**