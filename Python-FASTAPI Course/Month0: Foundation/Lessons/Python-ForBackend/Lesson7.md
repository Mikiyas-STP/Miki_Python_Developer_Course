# Topic 7: Context Managers (The `with` Statement)

As a backend engineer, you will deal with **Resources**:
1.  Database connections
2.  Files
3.  Network sockets

If you open a file but forget to close it, you create a **Memory Leak**. Eventually, your server will run out of "File Handles" and refuse to open anything else.

#### 1. The Old (Bad) Way
```python
f = open("log.txt", "w")
f.write("Hello")
# If the code crashes HERE, the file stays open forever!
f.close()
```

#### 2. The Professional Way: `with`
The `with` statement ensures the resource is **automatically closed**, even if your code crashes in the middle.

```python
with open("log.txt", "w") as f:
    f.write("Hello")
# The file is closed automatically the moment the 'with' block ends.
```

#### 3. Creating Your Own (The `@contextmanager` decorator)
Sometimes you need a context manager for your own logic (e.g., a "Timer" or a "Database Transaction"). We use a generator for this!

```python
from contextlib import contextmanager

@contextmanager
def database_connection():
    print("--- CONNECTING TO DB ---")
    yield "CONNECTION_OBJECT" # The 'resource' we give to the 'with' block
    print("--- DISCONNECTING FROM DB ---")

# Usage
with database_connection() as conn:
    print(f"Using {conn} to save data...")
```

---

### Your Coding Challenge: The "Audit Logger"

You want to create a context manager that logs when an "Admin Action" starts and when it finishes.

**Task:**
1.  Use the `@contextmanager` decorator.
2.  Create a function called `admin_session`.
3.  It should take a `user_name` string.
4.  **Logic:**
    *   When the block **starts**: Print `"AUDIT: User [name] started a session."`
    *   **Yield** nothing (just `yield`).
    *   When the block **ends**: Print `"AUDIT: User [name] closed the session."`

**Starter Code:**
```python
from contextlib import contextmanager

# TODO: Create the admin_session context manager
def admin_session(user_name):
    pass

# How it should be used:
with admin_session("Alice") as session:
    print("   Alice is deleting old logs...")
    print("   Alice is updating user permissions...")

# Output should be:
# AUDIT: User Alice started a session.
#    Alice is deleting old logs...
#    Alice is updating user permissions...
# AUDIT: User Alice closed the session.
```

**Show me your Context Manager!** This is the gold standard for writing safe backend code.
**Answer in 13contextmanager.py** 