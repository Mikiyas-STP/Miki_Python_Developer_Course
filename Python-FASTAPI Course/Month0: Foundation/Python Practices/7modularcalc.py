def math_operation(a:int ,b:int ,**kwargs)-> dict:
    result = a + b
    return {"result":result} | kwargs

if __name__=="__main__":
    print(math_operation(1,2,user="admin"))



# This is a very clean and professional-looking module! You nailed the `if __name__ == "__main__":` block and the dictionary merging logic. 

# However, we need to do a **Senior Code Review** because you missed one specific requirement: the `operation` logic. This is actually a perfect opportunity to teach you about **Argument Ordering** in Python.

# ### 🚩 Code Review

# **1. Missing Argument & Logic**
# *   **The Issue:** Your function only does addition. We wanted it to handle "add" or "mul" (multiplication) based on an `operation` argument.
# *   **The Fix:** We need to add `operation="add"` to the function signature.

# **2. The "Argument Order" Rule**
# In Python, there is a very strict order for function parameters:
# 1.  **Positional arguments** (`a, b`)
# 2.  **Default/Keyword arguments** (`operation="add"`)
# 3.  **Variable arguments** (`*args`)
# 4.  **Keyword-variable arguments** (`**kwargs`) — **This must ALWAYS be last.**

# ---

# ### Refactoring your code:

# Here is how the professional version of that function looks. Notice how `operation` is explicitly named, so it **doesn't** end up inside the `kwargs` dictionary.

# ```python
def math_operation(a: int, b: int, operation: str = "add", **kwargs) -> dict:
    # 1. Handle the specific logic
    if operation == "add":
        result = a + b
    elif operation == "mul":
        result = a * b
    else:
        result = 0  # Or handle error
        
    # 2. Return the result plus any extra metadata
    # Metadata is in kwargs; result is its own key
    return {"result": result} | kwargs

if __name__ == "__main__":
    # Test 1: Default addition
    print(math_operation(5, 5, user="admin")) 
    # Output: {'result': 10, 'user': 'admin'}

    # Test 2: Explicit multiplication
    print(math_operation(5, 5, operation="mul", session_id=99))
    # Output: {'result': 25, 'session_id': 99}
# ```

# ---

# ### 🧠 Deep Question: Understanding the Boundary

# In **Test 2** above, I passed `operation="mul"`. 
# **Does the word `"mul"` exist inside the `kwargs` dictionary in that function call?** 

# Think carefully! If a parameter is explicitly defined in the function (like `operation`), Python treats it as a local variable. `**kwargs` only catches the "leftovers."
