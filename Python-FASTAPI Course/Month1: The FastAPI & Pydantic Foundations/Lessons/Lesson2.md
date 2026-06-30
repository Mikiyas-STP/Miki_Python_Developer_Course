### Month 1, Week 2: Dependency Injection (DI)

Before we move to the next coding challenge, we need to talk about **Dependency Injection**. This sounds like a scary word, but it is a very simple concept that makes your backend modular.

**The Concept:**
Sometimes your routes need "Help." They might need:
*   A database connection.
*   A way to check if a user is logged in.
*   A logger.

Instead of creating these things *inside* every function, we "Inject" them.

**How it looks in FastAPI:**
We use `Depends`.

```python
from fastapi import Depends

# A simple "Helper" function
def get_query_token(token: str | None = None):
    if not token:
        return "No token provided"
    return token

@app.get("/items")
async def read_items(token_status: str = Depends(get_query_token)):
    return {"token_is": token_status}
```

**Why do we do this?**
It makes testing easy! When you are testing your code, you can "inject" a fake database instead of a real one without changing your function logic.

---

### Your Next Challenge: The "Secure AI Guard"

Let's combine **Pydantic Validation** with a simple **Dependency**.

**Task:**
1.  Create a "Dependency" function called `verify_api_key`. It should look for a query parameter called `api_key` (str).
    *   If the key is `"london-python"`, return `True`.
    *   Otherwise, return `False`.
2.  Update your `/process-prompt` route to use this dependency.
3.  **Logic:** 
    *   If the dependency returns `True`, process the prompt normally.
    *   If `False`, return a `401 Unauthorized` status (Hint: Use `from fastapi import HTTPException`).

**Does the concept of "Injecting" a helper into a function make sense to you?** Try to write the code for this!