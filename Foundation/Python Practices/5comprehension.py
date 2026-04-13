
# #### Challenge B: Inventory Value (Dictionary Comprehension)
# You are building an inventory management system. You have a dictionary of products and their prices.
# ```python
# inventory = {
#     "laptop": 1200,
#     "mouse": 25,
#     "keyboard": 80,
#     "monitor": 300
# }
# **Task:** Write a function `apply_discount(items: dict) -> dict` that:
# 1.  Creates a new dictionary.
# 2.  If the price is **over 100**, apply a 10% discount (multiply by `0.9`).
# 3.  If the price is **100 or less**, keep the original price.

# **Goal Result:** `{'laptop': 1080.0, 'mouse': 25, 'keyboard': 80, 'monitor': 270.0}`

# ---

# ### One Question to Test your Logic:
# In the `clean_emails` challenge, why should you check if the email is `None` **before** you try to call `.strip()` or `.lower()`? (What happens if you call a method on `None` in Python?)

# **Show me your two functions!**
# This two challanges are #4 and #5 in the basic python practices
def apply_discount(items: dict) -> dict:
    return {
        key: value * 0.9 if value > 100 else value
        for key, value in items.items()
    }