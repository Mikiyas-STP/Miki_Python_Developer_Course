
# Topic 2: Functions, Type Hints, and Clean Code

You’ve mastered the data structures. Now we need to talk about how we structure **Functions** in a professional backend environment. 

In a real API, you don't always know exactly how many arguments you are going to get. For example, a search function might have 1 filter or 10 filters.

### Concept 1: `*args` and `**kwargs`
These look scary, but they are just "catch-all" buckets for arguments.

*   **`*args` (Arguments):** Collects extra positional arguments into a **Tuple**.
*   **`**kwargs` (Keyword Arguments):** Collects extra named arguments into a **Dictionary**.

**Backend Example:** A logging function that accepts a message and then any amount of extra metadata.

```python
def log_event(message: str, **metadata):
    print(f"LOG: {message}")
    for key, value in metadata.items():
        print(f"--- {key}: {value}")

# We can pass any named arguments we want!
log_event("User Login", user_id=101, ip="1.1.1.1", browser="Chrome")
```

### Concept 2: Type Hinting `Optional` and `Union`
In backend dev, data is often missing. A user might have a `middle_name`, or they might not.
We use the `|` (OR) symbol in modern Python (3.10+) to show multiple possible types.

```python
# This means: name can be a string OR it can be None
def greet(name: str | None = None):
    if name:
        return f"Hello {name}"
    return "Hello Guest"
```

---

### Your Coding Challenge: The "Flexible API Query Builder"

You are writing a helper function for a database. The function should take a `table_name` and then any number of "filters" (which will be passed as keyword arguments).

**Task:**
Write a function `build_query(table: str, **filters) -> str`.
1.  The function should return a string.
2.  It should start with `"SELECT * FROM [table_name] WHERE "`.
3.  It should then list the filters in the format `key='value'`.

**Example of how it should work:**
```python
query = build_query("users", status="active", role="admin")
print(query)
# Expected Output: "SELECT * FROM users WHERE status='active', role='admin'"
```

**Wait!** Before you start, a **Senior Tip**: 
To turn a dictionary into a string like `key='value', key='value'`, you can use a list comprehension and `.join()`.
Example: `", ".join([f"{k}='{v}'" for k, v in filters.items()])`

**Let's see if you can put the `**kwargs` and the `.join()` together!**


**Answer:**
```python
def build_query(table: str, **filters) -> str:
    conditions = ", ".join([f"{k}='{v}'" for k, v in filters.items()])
    return f"SELECT * FROM {table} WHERE {conditions}"
```





Let’s refine your mental model of the two types of logic we use in comprehensions.

---

### The Two Faces of Comprehensions

There are two places you can put logic in a comprehension. This is where most people get confused.

#### 1. The "Filter" (At the end)
This decides **if** an item should even be in the final result.
*   **Syntax:** `[item for item in list if condition]`
*   **Backend Example:** Get only successful transactions.

#### 2. The "Transformation" (At the beginning)
This decides **what** the item looks like (e.g., mapping). This is where you can use an `if-else` block.
*   **Syntax:** `[x if condition else y for x in list]`
*   **Backend Example:** Masking sensitive data (If user is admin, show email; else, show "HIDDEN").

---

### Real-World Example: User Permission Mapping

Imagine you are preparing a list of users for a frontend table. You need to mark them as "Authorized" or "Guest".

```python
users = ["Alice", "Bob", "Charlie", "Dave"]
admins = ["Alice", "Charlie"]

# Goal: Create a list where it shows 'Authorized' if in admins, else 'Guest'
status_list = ["Authorized" if user in admins else "Guest" for user in users]

print(status_list) 
# ['Authorized', 'Guest', 'Authorized', 'Guest']
```

---

### Your Deep-Dive Challenges

I have two challenges for you. One for Lists, one for Dictionaries.

#### Challenge A: The Email Sanitizer (List Comprehension)
You have a list of user-submitted emails. Some are empty (`None`), some have extra spaces, and some are uppercase.

```python
raw_emails = [" ALICE@gmail.com ", None, "bob@TEST.com", "  ", "CHARLIE@DEV.IO"]
```

**Task:** Write a function `clean_emails(emails: list) -> list` that:
1.  Filters out any emails that are `None` or just empty whitespace strings. (Hint: `.strip()` on an empty string ` " " ` makes it "falsy").
2.  Returns a list where all remaining emails are **lowercase** and **stripped** of whitespace.

---

#### Challenge B: Inventory Value (Dictionary Comprehension)
You are building an inventory management system. You have a dictionary of products and their prices.

```python
inventory = {
    "laptop": 1200,
    "mouse": 25,
    "keyboard": 80,
    "monitor": 300
}
```

**Task:** Write a function `apply_discount(items: dict) -> dict` that:
1.  Creates a new dictionary.
2.  If the price is **over 100**, apply a 10% discount (multiply by `0.9`).
3.  If the price is **100 or less**, keep the original price.

**Goal Result:** `{'laptop': 1080.0, 'mouse': 25, 'keyboard': 80, 'monitor': 270.0}`

---

### One Question to Test your Logic:
In the `clean_emails` challenge, why should you check if the email is `None` **before** you try to call `.strip()` or `.lower()`? (What happens if you call a method on `None` in Python?)

**Show me your two functions!**
This two challanges are #4 and #5 in the basic python practices















# Topic 2: Functions, Type Hints, and Clean Code

You’ve mastered the data structures. Now we need to talk about how we structure **Functions** in a professional backend environment. 

In a real API, you don't always know exactly how many arguments you are going to get. For example, a search function might have 1 filter or 10 filters.

### Concept 1: `*args` and `**kwargs`
These look scary, but they are just "catch-all" buckets for arguments.

*   **`*args` (Arguments):** Collects extra positional arguments into a **Tuple**.
*   **`**kwargs` (Keyword Arguments):** Collects extra named arguments into a **Dictionary**.

**Backend Example:** A logging function that accepts a message and then any amount of extra metadata.

```python
def log_event(message: str, **metadata):
    print(f"LOG: {message}")
    for key, value in metadata.items():
        print(f"--- {key}: {value}")

# We can pass any named arguments we want!
log_event("User Login", user_id=101, ip="1.1.1.1", browser="Chrome")
```

### Concept 2: Type Hinting `Optional` and `Union`
In backend dev, data is often missing. A user might have a `middle_name`, or they might not.
We use the `|` (OR) symbol in modern Python (3.10+) to show multiple possible types.

```python
# This means: name can be a string OR it can be None
def greet(name: str | None = None):
    if name:
        return f"Hello {name}"
    return "Hello Guest"
```

---

### Your Coding Challenge: The "Flexible API Query Builder"

You are writing a helper function for a database. The function should take a `table_name` and then any number of "filters" (which will be passed as keyword arguments).

**Task:**
Write a function `build_query(table: str, **filters) -> str`.
1.  The function should return a string.
2.  It should start with `"SELECT * FROM [table_name] WHERE "`.
3.  It should then list the filters in the format `key='value'`.

**Example of how it should work:**
```python
query = build_query("users", status="active", role="admin")
print(query)
# Expected Output: "SELECT * FROM users WHERE status='active', role='admin'"
```

**Wait!** Before you start, a **Senior Tip**: 
To turn a dictionary into a string like `key='value', key='value'`, you can use a list comprehension and `.join()`.
Example: `", ".join([f"{k}='{v}'" for k, v in filters.items()])`

**Let's see if you can put the `**kwargs` and the `.join()` together!**


**Answer**
```
def generate_search_summary(search_term: str, **kwargs) -> str:
    if not kwargs:
        return f"Searching for '{search_term}' with no filters"
    
    filters_str = ", ".join([f"{key}={value}" for key, value in kwargs.items()])
    return f"Searching for '{search_term}' with filters: {filters_str}"

```







let's demystify the **`**kwargs` magic** before we move on.

---

### The "Magic" of `**kwargs` Explained

Think of `**kwargs` (Keyword Arguments) as a **dictionary builder**.

When you call a function like this:
`generate_search_summary("Laptop", category="Electronics", stock=10)`

1. Python sees the first argument `"Laptop"` and puts it in the `search_term` variable.
2. Python sees `category="Electronics"` and `stock=10`. Because they have names (keys) and values, and you have `**kwargs` in your function definition, Python says: *"Okay, let's put these in a dictionary."*
3. Inside your function, `kwargs` literally becomes: `{"category": "Electronics", "stock": 10}`.

**In JavaScript terms:**
This is very similar to "Rest parameters" in an object:
```javascript
// JS Equivalent
function generateSummary(searchTerm, ...kwargs) { 
    // In JS, kwargs would be an array, but if we passed an object:
    // const {searchTerm, ...filters} = data;
}
```

---

### The Next Level: Unpacking (The `**` on the other side)

We just saw how `**` **collects** arguments into a dictionary. But in backend engineering, we often do the opposite: **Unpacking**.

Imagine you have a dictionary (maybe from a JSON API) and a function that expects specific arguments. Instead of passing them one by one, you "unpack" the dictionary into the function.

```python
def create_api_user(username: str, role: str, email: str):
    print(f"Creating {role}: {username} ({email})")

# Data from an API/Database
user_data = {
    "username": "sara_dev",
    "role": "admin",
    "email": "sara@company.com"
}

# Instead of: create_api_user(user_data["username"], user_data["role"]...)
# We do this:
create_api_user(**user_data) 
```
The `**` tells Python: *"Take this dictionary and match the keys to the function's arguments."*

---

### Coding Exercise: The "User Updater"

Let's practice both **collecting** and **unpacking**. 

**Scenario:** 
You are building a profile update system. You have a "Database" (just a dictionary for now). You need a function that takes the current user and applies only the changes provided.

**Task:**
1. Create a function `update_profile`.
2. It should take two arguments:
   * `current_profile: dict` (The current user data)
   * `**updates` (Any number of changes the user wants to make)
3. Inside the function, use the `.update()` method (a dictionary method) to merge the `updates` into the `current_profile`.
4. Return the updated dictionary.

**Starter Code:**
```python
user_profile = {
    "username": "coder_123",
    "email": "old@email.com",
    "bio": "Hello world"
}

# TODO: Write the update_profile function
def 

# TEST: We want to change the email and bio, but keep the username the same.
new_profile = update_profile(user_profile, email="new@email.com", bio="Python pro")

print(new_profile)
# Expected: {'username': 'coder_123', 'email': 'new@email.com', 'bio': 'Python pro'}
```

---

### Follow-up Questions to test understanding:

1. In your `generate_search_summary` code, what would happen if you forgot the `**` and just wrote `def generate_search_summary(search_term, kwargs):`? Would it still work the same way?
2. If I called `update_profile(user_profile, age=25)`, and "age" wasn't in the original profile, would it be added or would it crash? (Try to guess based on how you think dictionaries work!)

**Answer is available in basicpython folder 6updateprofile.py**
