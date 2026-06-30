### Topic 3: Python Modules and Project Structure

You are getting very good at writing individual functions. But in a real backend job, you don't have one giant file. You have hundreds.

**Concept: The `if __name__ == "__main__":` Block**
In Python, every file is a "Module." When you `import` a file, Python runs all the code in it. 
To prevent your test code (like `print(update_profile(...))`) from running when you import the function into another file, we use this special check.

**Example of a professional file structure (`user_service.py`):**

```python
def update_profile(profile: dict, **updates) -> dict:
    return profile | updates

# This block ONLY runs if you play/run THIS file directly.
# It will NOT run if you import this file into a web server.
if __name__ == "__main__":
    test_user = {"name": "Dev"}
    print(update_profile(test_user, role="admin"))
```

---

### Your Coding Challenge: The "Modular Calculator"

I want you to simulate a small project. 

**Task:**
1.  Define a function called `math_operation`.
2.  It should take two required numbers: `a` and `b`.
3.  It should take a keyword argument called `operation` (default it to `"add"`).
4.  It should use `**kwargs` to accept "metadata" (like `user="admin"`, `timestamp="12:00"`).
5.  **Logic:**
    *   If `operation` is `"add"`, result is `a + b`.
    *   If `operation` is `"mul"`, result is `a * b`.
6.  **Return:** A dictionary containing the `result` and all the `metadata` from `kwargs`.

**Wrap your test code in an `if __name__ == "__main__":` block.**

**Senior Hint:** You can merge the result into the kwargs dict easily: `return {"result": result} | kwargs`

**answer in 7modularcal.py!**