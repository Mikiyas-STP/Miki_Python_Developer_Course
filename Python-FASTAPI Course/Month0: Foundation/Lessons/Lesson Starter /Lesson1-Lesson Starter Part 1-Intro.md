**Python Crash Course for JS Developers**. 
### The Complete Python Syntax Overview

#### 1. Variables and Types
In Python, there is no `let` or `const`. You just declare the variable. Also, `true`, `false`, and `null` are capitalized or changed.
```python
# Strings, Integers, Floats
name = "Alice"
age = 28
price = 19.99

# Booleans (Must be capitalized in Python!)
is_active = True
has_error = False

# Null/Undefined equivalent
user_data = None 
```

#### 2. The Core Data Structures (Collections)
Backend engineering is mostly moving and reshaping data. These are the four containers you will use every day.

**A. Lists (JS Arrays)**
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # JS .push()
print(len(fruits))       # JS fruits.length
```

**B. Dictionaries (JS Objects / JSON)**
Keys and values. You *must* use strings for keys and access them with brackets.
```python
user = {
    "id": 1,
    "email": "alice@example.com"
}
# Reading a value
print(user["email"])  

# Adding/Updating a value
user["is_admin"] = True 
```

**C. Tuples (Strict Lists)**
A tuple is just a list that **cannot be changed** (immutable) after you create it. We use parentheses `()` instead of brackets `[]`.
```python
coordinates = (10.5, 20.1)
# coordinates.append(5.0) -> This would crash! Tuples are locked.
```

**D. Sets**
Just like in JS, a Set is a collection of unique items. Great for removing duplicates.
```python
unique_numbers = {1, 2, 2, 3}
print(unique_numbers) # Output: {1, 2, 3}
```

#### 3. Control Flow (If statements and Loops)
Python relies on **indentation** (spaces) to know what code belongs inside an `if` statement or loop. No curly braces `{}`.

**If / Else If / Else**
```python
status_code = 404

if status_code == 200:
    print("Success!")
elif status_code == 404:     # 'elif' is Python for 'else if'
    print("Not Found")
else:
    print("Server Error")
```

**For Loops** (Python loops iterate *over* things directly, like JS `for...of`)
```python
names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(name)
```

#### 4. Functions & Type Hints (Modern Backend)
In professional Python backend code (like FastAPI), we use **Type Hints**. They don't change how the code runs, but they tell other developers (and your code editor) what type of data is expected.

```python
# def means "define function"
# name: str means "name should be a string"
# -> str means "this function returns a string"

def greet_user(name: str) -> str:
    return f"Hello, {name}!"  # f-strings are like JS template literals (`Hello, ${name}!`)
```

---

### Let's practice the basics together.

I want you to write a very standard, foundational backend function. No advanced tricks, no one-liners. Just straightforward logic using the rules above.

**The Scenario:**
You are building a registration endpoint. You need to write a function that takes a user's name and age, and creates a dictionary for them.

**The Rules:**
1. Create a function called `create_user_profile`.
2. It should accept two parameters: `name` (a string) and `age` (an integer).
3. Inside the function, write an `if/else` statement:
   * If the age is 18 or older, create a variable called `is_adult` and set it to `True`.
   * If the age is under 18, set `is_adult` to `False`.
4. The function must return a dictionary that looks exactly like this:
   `{"name": "the_name_passed_in", "age": the_age_passed_in, "is_adult": True_or_False}`

**Example of how it should work when you are done:**
```python
profile = create_user_profile("David", 16)
print(profile) 
# Should print: {'name': 'David', 'age': 16, 'is_adult': False}
```
```

**Solution:**
def create_user_profile(name, age):
    if age >= 18:
        is_adult = True
    else:
        is_adult = False

    user_profile = {
        "name": name,
        "age": age,
        "is_adult": is_adult
    }

    return user_profile

```