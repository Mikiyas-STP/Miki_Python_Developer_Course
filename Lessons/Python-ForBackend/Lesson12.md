**Integration Testing** is testing how different parts of your system work **together**.

- **Unit Testing** (The opposite): Testing one tiny piece in isolation (e.g., _Does this specific math function work?_).
- **Integration Testing**: Testing the "handshake" between parts (e.g., _Does my **Function** successfully send data to my **Database**?_).

In the code I gave you, the "Integration" is seeing how the **Decorator**, the **Class**, and the **Async loop** all talk to each other to finish one task.

Let's build a **"User Activity Monitoring Service."** This is a very common backend task: fetching data from a database, checking permissions, processing logs in batches, and handling errors if the system is down.

Below is a single script. I have labeled where each of the **11 Topics** is being used.

### The "Big Picture" Script

```python
import asyncio
import logging
from contextlib import contextmanager
from typing import List, Dict, Optional # Topic 2: Type Hints

# Topic 8: Error Handling & Logging Setup
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Topic 5: Decorators (The Security Guard)
def authenticated(func):
    async def wrapper(user_obj, *args, **kwargs):
        if not user_obj.is_active:
            logging.warning(f"Unauthorized access attempt by {user_obj.username}")
            return "Access Denied"
        return await func(user_obj, *args, **kwargs)
    return wrapper

# Topic 4: Object-Oriented Programming (The User Model)
class User:
    def __init__(self, username: str, is_active: bool = True):
        self.username = username
        self.is_active = is_active
        self.tags: set[str] = set() # Topic 1: Using a Set for unique data

# Topic 7: Context Managers (Safe Database Connection)
@contextmanager
def database_session():
    try:
        logging.info("--- [DB] Opening Connection ---")
        yield "DB_SESSION_ACTIVE"
    finally:
        logging.info("--- [DB] Closing Connection Safely ---")

# Topic 6: Generators (Efficiently processing massive logs)
def process_activity_logs(logs: List[str]):
    for i in range(0, len(logs), 2): # Batching logic
        yield logs[i:i+2]

# Topic 11: Production-Ready Logic (A Service Class)
class UserActivityService:
    def __init__(self, user: User):
        self.user = user

    # Topic 10: Asynchronous Python (Non-blocking DB fetch)
    @authenticated # Topic 5 again
    async def fetch_dashboard_data(self) -> str:
        with database_session() as session: # Topic 7 again
            await asyncio.sleep(1) # Simulating network delay
            return f"Dashboard data for {self.user.username} loaded via {session}."

# Topic 3: Project Structure Entry Point
async def main():
    # Setup some dummy data (Topic 1: Data Structures)
    raw_logs = ["Login", "ViewHome", "UpdateProfile", "Logout", "SearchProduct"]

    # Topic 8: Handling the "Happy Path" and "Error Path"
    try:
        # Create user instance
        current_user = User("alice_dev", is_active=True)
        service = UserActivityService(current_user)

        # 1. Run Async Action
        print("Fetching data...")
        result = await service.fetch_dashboard_data()
        print(f"Result: {result}")

        # 2. Process Logs using the Generator
        print("\nProcessing logs in batches:")
        for batch in process_activity_logs(raw_logs):
            print(f"Processing: {batch}")

    except Exception as e:
        logging.error(f"A system error occurred: {e}")

if __name__ == "__main__":
    # Topic 9: (Conceptual) This would run inside your Virtual Environment
    asyncio.run(main())
```

---

### The "Bridge" Map: How these topics connect

1.  **Topics 1 & 4 (Data & Objects):** We defined what a `User` looks like. In a real backend, this is your "Database Model."
2.  **Topics 5 & 11 (Decorators & Clean Code):** Notice how we put the security check (`@authenticated`) _outside_ the logic. This means the `fetch_dashboard_data` function only cares about data, not security.
3.  **Topics 7 & 8 (Context & Errors):** Even if the `await asyncio.sleep` crashed, the `finally` block in our context manager ensures the database connection closes.
4.  **Topic 6 (Generators):** If `raw_logs` had 1 million items, our server wouldn't crash because we `yield` small batches.
5.  **Topic 10 (Async):** The whole program runs inside `asyncio.run(main())`, meaning our server can handle other requests while Alice's dashboard is "loading."

---

### Your Turn: The "Integration Test" Challenge

I want you to make **one small change** to the code above to prove you see how the pieces fit together.

**The Task:**
Modify the `authenticated` decorator logic.
Currently, it only checks `user_obj.is_active`. I want you to change it so it also checks if the user has a specific "tag" called `"admin"`.

1.  Add a line to `User.__init__` to add `"admin"` to `self.tags` for testing.
2.  Update the `if` statement in the `authenticated` decorator to check: `if not user_obj.is_active or "admin" not in user_obj.tags:`.

**Why am I asking this?**
Because in a real API, this is exactly how you handle "Role Based Access Control" (RBAC). It combines **Data Structures (Topic 1)**, **OOP (Topic 4)**, and **Decorators (Topic 5)**.

**Try to rewrite just those two parts and show me. Does the "Big Picture" feel a little clearer now?**
