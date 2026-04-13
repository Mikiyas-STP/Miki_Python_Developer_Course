# Topic 8: Error Handling and Logging

In backend development, your code runs on a server. You are not there to watch it. If the code "crashes" (stops working), the whole website goes down. 

A **Junior Developer** knows how to stop a crash.
A **Mid-Level Developer** knows how to record *why* it crashed so they can fix it later.

---

### 1. The Junior Level: `try`, `except`, and `raise`

Imagine you are building a function to **divide money** among users.

#### The Problem: The Crash
If a user tries to divide money by zero, Python doesn't know what to do. It stops the program. We call this an **Exception**.

#### The Tool: `try` and `except`
We use `try` to wrap the "dangerous" code. We use `except` to say what to do if it breaks.

```python
def share_money(total_money, total_people):
    try:
        # This is the dangerous part
        result = total_money / total_people
        return result
    except ZeroDivisionError:
        # If the dangerous part breaks, do this instead
        return "Error: You cannot share money with zero people."
```

#### The Tool: `raise` (The Alarm)
Sometimes, the code isn't "broken," but the data is "wrong." For example, if someone tries to share **negative** money. Python doesn't mind negative numbers, but a bank does! We use `raise` to trigger our own alarm.

```python
def check_amount(amount):
    if amount < 0:
        # We trigger the alarm manually
        raise ValueError("Money cannot be negative!")
```

---

### 2. The Mid-Level Level: `else`, `finally`, and `logging`

A mid-level developer thinks about **cleanup** and **records**.

#### `finally` (The Cleanup)
In the backend, you often open a "Connection" to a Database. Even if your code crashes, you **must** close that connection, or the server will get tired and slow. `finally` runs **no matter what**.

#### `else` (The Success Path)
The `else` block runs only if the `try` block was a 100% success. It keeps your code organized.

#### `logging` (The Record)
In a real company, we don't use `print()`. We use `logging`.
*   `logging.info()`: "Everything is fine."
*   `logging.warning()`: "Something is strange, look at this."
*   `logging.error()`: "Something broke!"

---

### 3. The Pythonic Perspective: EAFP

In JavaScript, you might check things before you do them:
`if (user exists) { do something }`

In Python, we use **EAFP**: *Easier to Ask for Forgiveness than Permission.*
We "Try" to do it. If the user doesn't exist, the `except` block catches it. This is faster and more "Pythonic" for backend work.

---

### Real-World Backend Example: Database Loader

Imagine you are loading a user's settings from a file.

```python
import logging

# Setup the "Recorder" (Logger)
logging.basicConfig(level=logging.INFO)

def load_user_config(file_name):
    print(f"--- Attempting to load {file_name} ---")
    try:
        # 1. Dangerous action: Opening a file
        file = open(file_name, "r")
        data = file.read()
    except FileNotFoundError:
        # 2. Safety Net: If file is missing
        logging.error(f"The file {file_name} was not found!")
        return {}
    else:
        # 3. Success: Runs ONLY if file was opened correctly
        logging.info("Config loaded successfully.")
        return data
    finally:
        # 4. Cleanup: Always runs to keep the server clean
        print("Cleaning up system resources...")
```

---

### Your Coding Challenge: The "Secure Database Search"

You are building a search tool for a database. 

**Task:**
1.  Create a function `get_db_record(record_id: int)`. 
    *   If `record_id` is **0**, use `raise` to trigger a `ValueError` with the message `"ID 0 is reserved"`.
    *   If `record_id` is **99**, use `raise` to trigger a `ConnectionError` with the message `"Database Offline"`.
    *   Otherwise, return `"Record Data"`.

2.  Create a function `run_search(record_id: int)`.
    *   Use a **`try`** block to call `get_db_record`.
    *   **`except ValueError`**: Use `logging.warning()` to log the error and return `None`.
    *   **`except ConnectionError`**: Use `logging.error()` to log the error and return `None`.
    *   **`else`**: Use `logging.info()` to log `"Search Successful"`.
    *   **`finally`**: Use `print()` to say `"Database connection closed."`

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# TODO: Write your functions here
```

---

### Follow-up Questions:
1.  Why is `finally` important when we are working with files or databases?
2.  What is the difference between `logging.warning()` and `logging.error()` in a real application? (Which one is more serious?)

**Take your time. Focus on getting the structure of the `try/except/else/finally` block right.**


### Answer is in 14errorhandling.py

### 🎓 Topic 8 Summary (What you have learned)

# You have completed the core knowledge for Error Handling. You now know:
* How to **detect** errors (`try`).
* How to **handle** specific errors (`except NameOfError as e`).
* How to **run** code only on success (`else`).
* How to **manually trigger** an alarm (`raise`).
* How to **record** events for other engineers (`logging`).