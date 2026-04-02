# Topic 10: Asynchronous Python (async/await)

This is the **"Final Boss"** of Python backend development. Modern frameworks like **FastAPI** are built entirely on this.

### The Problem: The "Waiting" Game
In a normal (synchronous) backend, if a user requests a large file from a database, the server **stops and waits**. It cannot talk to any other users until the database finishes. This is slow.

### The Solution: `async` (Multi-tasking)
Imagine a waiter in a restaurant:
*   **Sync Waiter:** Takes an order, goes to the kitchen, and **stands there** until the food is ready. He ignores all other customers.
*   **Async Waiter:** Takes an order, gives it to the kitchen, and then **immediately** goes to help other customers while the food is cooking.

#### 1. Defining an Async Function
We use the keyword `async def`. This creates a **Coroutine**.

#### 2. The `await` Keyword
We use `await` when we call a function that takes time (like a database query). It tells Python: *"You can go do other things while this finishes."*

```python
import asyncio

async def fetch_from_db():
    print("--- Database: Starting query... ---")
    await asyncio.sleep(2) # Simulates a 2-second wait
    return "User Data"

async def main():
    print("Main: Doing other work...")
    # We 'await' the result here
    data = await fetch_from_db()
    print(f"Main: Received {data}")

# To run an async program:
asyncio.run(main())
```

---

### Real-World Backend Example: Parallel API Calls

Imagine you need to get data from **Stripe** and **PayPal** at the same time.

```python
import asyncio

async def call_stripe():
    await asyncio.sleep(1)
    return "Stripe Success"

async def call_paypal():
    await asyncio.sleep(1)
    return "PayPal Success"

async def process_payments():
    # 'gather' runs them both AT THE SAME TIME
    results = await asyncio.gather(call_stripe(), call_paypal())
    print(results) # ['Stripe Success', 'PayPal Success']

asyncio.run(process_payments())
```
**Sync time:** 2 seconds. **Async time:** 1 second!

---

### Your Coding Challenge: The "Async Welcome"

You are building a login system. When a user logs in, you need to:
1.  Check the database (takes 1 second).
2.  Send a welcome email (takes 1 second).

**Task:**
1.  Create an `async` function `check_db(user: str)`. It should `await asyncio.sleep(1)` and return `"User Verified"`.
2.  Create an `async` function `send_email(user: str)`. It should `await asyncio.sleep(1)` and return `"Email Sent"`.
3.  Create an `async` function `login(user: str)`. 
    *   It should use `await asyncio.gather()` to run both functions **at the same time**.
    *   Print the results.

```python
import asyncio

# TODO: Write your three async functions here

if __name__ == "__main__":
    asyncio.run(login("David"))
```

---

### Follow-up Questions (B1 English):
1.  In your own words, what is the difference between a "Synchronous" waiter and an "Asynchronous" waiter?
2.  Why do we use `await` before calling a function like `asyncio.sleep(1)`? What happens if we forget the `await`?

**Take your time. This is a very new way of thinking about code!**
** Answer in 16async.py **