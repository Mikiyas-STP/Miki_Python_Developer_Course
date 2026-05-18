# ### Your Next Mini-Challenge: The "Input Validator"
# In backend development, we always validate user input before saving it to a database.
# **Task:**
# 1.  Create a function `validate_username(name: str)`.
#     *   If the name is shorter than 3 characters, `raise ValueError("Name too short")`.
#     *   If the name contains the word "admin", `raise PermissionError("Cannot use 'admin' in name")`.
#     *   Otherwise, return the name.
# 2.  Create a function `register_user(name: str)`.
#     *   Use `try...except...else`.
#     *   Catch the `ValueError` and log it as a **warning**.
#     *   Catch the `PermissionError` and log it as an **error**.
#     *   In the `else` block, log `"User [name] registered!"` as **info**.
# **Junior Check:** Make sure you pass the `name` argument into your `validate_username` call!
# **Give it a try! You are getting much better at the logic.**
import logging

# Standard setup for logging
logging.basicConfig(level=logging.INFO)

def validate_username(name: str):
    # 1. Use len() instead of .length
    if len(name) < 3:
        raise ValueError("Name too short")
    
    # 2. Use 'in' instead of __contains__
    if "admin" in name.lower(): # .lower() makes it even safer!
        raise PermissionError("Cannot use 'admin' in name")
    
    return name
    
def register_user(name: str):
    try:
        validate_username(name)
    except ValueError as v:
        # 3. Use f-strings for logging
        logging.warning(f"Registration Warning: {v}")
    except PermissionError as p:
        logging.error(f"Security Block: {p}")
    else:
        # 4. Use logging.info instead of print
        logging.info(f"User {name} successfully registered!")

# Test it
register_user("ed")            # Too short -> WARNING
register_user("admin_bob")     # Has admin -> ERROR
register_user("david_coder")   # Valid -> INFO