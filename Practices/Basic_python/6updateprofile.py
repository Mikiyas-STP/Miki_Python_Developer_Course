### The Two Professional Solutions

# #### Option A: The `.update()` approach (Classic)
# Inside the function, `updates` is just a normal dictionary.

def update_profile(current_profile: dict, **updates) -> dict:
    # This modifies the dictionary 'in-place'
    current_profile.update(updates) 
    return current_profile


# #### Option B: The "Merge" approach (Modern Python 3.9+)
# This is very popular in modern backend code because it creates a **new** dictionary without touching the old one.
# ```python
def update_profile(current_profile: dict, **updates) -> dict:
    # The '|' operator merges two dictionaries
    return current_profile | updates
# ```

# ---

# ### Answering the Follow-up Questions

# **1. What if you forgot the `**` in the function definition?**
# If you wrote `def search(term, kwargs):`, the function would expect exactly **two** arguments. You would have to call it like this: `search("Laptop", {"category": "Electronics"})`. 
# By adding `**`, you allow the user to type `category="Electronics"` freely, and Python builds the dictionary for you. It makes the API much nicer for the person using your code.

# **2. What if "age" wasn't in the original profile?**
# Dictionaries are flexible! If you call `update_profile(user, age=25)`, Python will simply add the new key `age` to the dictionary. It will **not** crash. This is great for adding new fields to a user profile dynamically.
