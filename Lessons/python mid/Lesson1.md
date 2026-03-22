
# Topic 1: Python Data Structures and Idiomatic Python

Now that we have the syntax foundation, let's look at how a **Senior Backend Engineer** actually manipulates data. We often need more than just simple lists and dicts.

### Concept 1: Sets (The "Duplicate Killer")
In backend development, you'll often get a list of IDs and need to ensure they are unique (e.g., getting a list of unique tags from a database).
*   **JS:** `new Set([1, 1, 2])`
*   **Python:** `{1, 1, 2}` or `set(my_list)`

```python
raw_tags = ["python", "api", "python", "rest", "api"]
unique_tags = set(raw_tags)
print(unique_tags) # {'python', 'api', 'rest'}
```

### Concept 2: Dictionary Comprehensions
Just like the List Comprehension we touched on earlier, we can create dictionaries in a single line. This is extremely common when "mapping" database results.

**The Backend Example:**
Converting a list of users into a "lookup map" where the key is the ID and the value is the username.

```python
users = [
    {"id": 101, "name": "Alice"},
    {"id": 102, "name": "Bob"}
]

# {key_expression: value_expression for item in list}
user_lookup = {user["id"]: user["name"] for user in users}

print(user_lookup) # {101: 'Alice', 102: 'Bob'}
print(user_lookup[101]) # Instant lookup!
```

### Concept 3: The `f-string` for Formatting
We saw this briefly, but it's vital for logging.
```python
user = "admin_01"
action = "DELETE_USER"
print(f"AUDIT LOG: [User: {user.upper()}] performed [Action: {action}]")
```

---

### Real-world Backend Example: Data Normalization
Imagine you are receiving product names from a user-submitted form. The names are messy (extra spaces, mixed casing). You need to clean them up and remove duplicates before saving to the DB.

```python
raw_data = ["  laptop ", "mouSE", "LAPTOP", " Keyboard ", "mouse "]

# 1. Clean (strip and lowercase)
# 2. Set (remove duplicates)
cleaned_products = {p.strip().lower() for p in raw_data}

print(cleaned_products) # {'laptop', 'mouse', 'keyboard'}
```

---

### Coding Challenge: The API Data Formatter

You are building a report for a sales manager. You have a list of sales transactions.

```python
sales_data = [
    {"item": "Laptop", "price": 1200, "sold": True},
    {"item": "Mouse", "price": 25, "sold": False},
    {"item": "Keyboard", "price": 75, "sold": True},
    {"item": "Monitor", "price": 300, "sold": True},
]
```

**Task:**
Write a function `format_sales_report(data: list[dict]) -> dict` that does the following:
1.  Filters out any items that were **not** sold.
2.  Returns a **Dictionary Comprehension** where:
    *   The **key** is the item name (all UPPERCASE).
    *   The **value** is the price.

**Goal Result:**
`{'LAPTOP': 1200, 'KEYBOARD': 75, 'MONITOR': 300}`

**Follow-up Question:**
Why might a Backend Engineer use a `Set` instead of a `List` when checking if a specific API key exists in a collection of 1,000,000 keys? (Think about performance).

*Take your time. Try to use the Dictionary Comprehension one-liner if you can!*
```
def format_sales_report(data: list[dict]) -> dict:
    return {item["item_name"].upper():item["price"] for item in data if item["sold"]}

print(format_sales_report(sales_data))
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