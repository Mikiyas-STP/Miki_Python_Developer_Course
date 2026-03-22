user_logged_in = True

def is_authenticated(func):
    def wrapper(*args, **kwargs):
        if user_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access Denied: Please log in first.")
    return wrapper

@is_authenticated
def view_profile(username):
    print(f"Welcome to your profile, {username}!")

# view_profile("alice123")
# **Spot on!** Your code is 100% correct. You have successfully implemented your first functional decorator.

# To answer your question: **Yes, exactly.** 

# The main advantages of a decorator in a backend context are:

# 1.  **Security (Gatekeeping):** As you saw, the `wrapper` acts as a bouncer. If the condition isn't met, the original function `view_profile` is never even touched. It’s safe.
# 2.  **DRY (Don't Repeat Yourself):** Imagine you have 50 different functions: `view_profile`, `delete_account`, `change_password`, etc. Without a decorator, you would have to write `if not logged_in: return` inside **every single one** of those 50 functions. With a decorator, you write it **once** and just add `@is_authenticated` to the others.
# 3.  **Clean Code:** Your business logic (viewing a profile) stays separate from your security logic (checking a login).

# ---

# ### One "Senior" Detail: `functools.wraps`

# There is one tiny problem with your current decorator. In Python, every function has metadata (its name, its documentation, etc.).

# If you check `print(view_profile.__name__)` right now, it will print `"wrapper"`, not `"view_profile"`. This happens because the decorator replaced the original function with the wrapper. In a big backend project, this can break debugging tools.

# **The Fix:** We use a built-in decorator *inside* our decorator called `@wraps`.

# ```python
from functools import wraps

def is_authenticated(func):
    @wraps(func) # This copies the original name and metadata back!
    def wrapper(*args, **kwargs):
        if user_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access Denied")
    return wrapper