class CoffeeOrder:
    def __init__(self, customer_name: str, coffee_type: str):
        # We save these into the object's "Memory" using self
        self.customer_name = customer_name
        self.coffee_type = coffee_type
        self.is_ready = False # Set to False by default inside the constructor

    def complete_order(self):
        # We update the object's memory
        self.is_ready = True

    def get_status(self) -> str:
        # We check the object's memory
        if self.is_ready:
            return f"Your {self.coffee_type} is ready, {self.customer_name}!"
        else:
            return "Still brewing..."

# --- Testing it ---
order1 = CoffeeOrder("Alice", "Latte")
print(order1.get_status())  # Still brewing...

order1.complete_order()     # This changes self.is_ready to True
print(order1.get_status())  # Your Latte is ready, Alice!


# ### 🧠 The "Why self?" Answer

# I asked you this earlier: **In `get_status`, why do we use `self.customer_name` instead of just `customer_name`?**

# **The Answer:** 
# Because `customer_name` (without `self`) only existed for a tiny moment inside the `__init__` method when the order was first created. Once `__init__` finished, that specific variable name disappeared.

# By writing `self.customer_name = customer_name`, you took that temporary piece of data and **nailed it to the object**. Now, every other method in the class can find it by looking at `self`.

# ---

# ### Let's try one more to solidify the "Memory" concept.

# In backend engineering, we often use objects to keep track of **Counts** or **States**.

# **The Scenario:** You are building a **Login Tracker**. You want to keep track of how many times a user has tried to log in so you can block them if they try too many times.

# **Task:**
# 1.  Create a Class called `LoginTracker`.
# 2.  In `__init__`, take a `username`.
# 3.  Also in `__init__`, create an attribute called `attempts` and set it to `0`. (Don't pass this as an argument).
# 4.  Create a Method called `register_fail`. This should **increase** `self.attempts` by 1.
# 5.  Create a Method called `is_blocked`. 
#     *   If `self.attempts` is 3 or more, return `True`.
#     *   Otherwise, return `False`.

# **Senior Tip:** To increase a number by one, use `self.attempts += 1`.

# **If you can do this, you’ve mastered the basics of how Objects "remember" things.** Give it a shot!

class LoginTracker:
    def __init__(self, username: str):
        self.username = username
        # Internal state - we don't let the outside world set this initially
        self.attempts = 0 

    def register_fail(self):
        self.attempts += 1

    def is_blocked(self) -> bool:
        # Simple, readable, professional
        return self.attempts >= 3

# --- How it works in memory ---
user1 = LoginTracker("alice_dev")
user1.register_fail()
user1.register_fail()
print(f"Is {user1.username} blocked? {user1.is_blocked()}") # False (attempts = 2)

user1.register_fail()
print(f"Is {user1.username} blocked? {user1.is_blocked()}") # True (attempts = 3)


