### Topic 4: Object-Oriented Programming (OOP) in Python

In backend engineering (especially with Django or SQLAlchemy), we use classes to represent **Models** (like a User, a Product, or an Order).

#### 1. The Anatomy of a Python Class
In JS, you have `constructor`. In Python, we have `__init__`.
In JS, you use `this`. In Python, we use `self`.

```python
class APIResponse:
    # The Constructor
    def __init__(self, status_code: int, data: dict):
        self.status_code = status_code  # Public attribute
        self.data = data

    # A method inside the class
    def is_success(self) -> bool:
        return 200 <= self.status_code < 300

# Usage
response = APIResponse(200, {"message": "Success"})
print(response.is_success()) # True
```

#### 2. Why `self`?
Every method in a Python class **must** take `self` as its first argument. `self` refers to the specific instance of the object. Python passes this automatically, so you don't provide it when calling the method.

---

### Your Coding Challenge: The "User Model"

Let's build a basic User model that you might find in a backend authentication system.

**Task:**
1. Create a class called `User`.
2. The `__init__` method should take `username`, `email`, and `role` (default role to `"guest"`).
3. Create a method called `get_profile`. It should return an f-string: `"User [username] is a [role]"`.
4. Create a method called `is_admin`. It should return `True` if the role is `"admin"`, otherwise `False`.

**Bonus Challenge (The Pythonic Way):**
Create a class variable called `VERSION` and set it to `1.0`.

**Structure:**
Wrap your test instances in the `if __name__ == "__main__":` block.

```python
class User:
    # TODO: Implement your class here
    pass

if __name__ == "__main__":
    # TODO: Create an admin user and a guest user, and print their profiles
    pass
```

**Show me your first Python Class!**


**Template to get you started:**
```python
class User:
    # TODO: Add a class variable 'VERSION' set to 1.0

    def __init__(self, username: str, email: str, role: str = "guest"):
        # TODO: Initialize your attributes here
        pass

    def get_profile(self) -> str:
        # TODO: Return the profile string
        pass

    def is_admin(self) -> bool:
        # TODO: Return True/False based on role
        pass

if __name__ == "__main__":
    # TODO: Create one admin user and one guest user
    # TODO: Print their profiles and check if they are admins
    pass
```

**Senior Hint:** Remember that every method inside a class **must** take `self` as the first argument. This is how the method "talks" to the specific user's data.

**Answer in 8class.py**



**question asked for the AI model for explanation and answer is here**
You are 100% right to stop me. I apologize—as a senior dev, sometimes I forget how strange the shift from "Functions" to "Objects" feels. Let's pull over, turn off the engine, and look at the map.

In your previous lessons, you wrote **Functions**. Functions are like **Recipes**: 
1. You give them ingredients (Arguments).
2. They follow steps (Logic).
3. They give you a result (Return).

**Object-Oriented Programming (OOP)** is different. It's about building **Packages** that contain both **Data** and **Actions** together.

---

### 1. Why do we need it? (The Problem)

Imagine you are building a Banking App. 

**Without OOP (Just Functions):**
You have variables for names and balances.
```python
user_name = "Alice"
user_balance = 1000

def withdraw(balance, amount):
    return balance - amount

user_balance = withdraw(user_balance, 500)
```
This is fine for *one* user. But what if you have 1,000,000 users? You'd have millions of loose variables floating around. It's easy to accidentally withdraw money from Alice's balance and give it to Bob's.

**With OOP (The Solution):**
You create a "package" called an **Account**. That package knows its own name and its own balance. You don't have to pass the balance into the function; the package already holds it.

---

### 2. The Vocabulary

*   **Class:** The **Blueprint**. It’s the paper drawing of a car. It isn't a car yet; it's just the *description* of what a car should have (wheels, engine, color).
*   **Instance (Object):** The **Actual Car**. If you use the blueprint to build a red Ford and a blue Chevy, those are two *instances* of the "Car" class.
*   **Attribute:** The **Data** inside the object (e.g., `color = "red"`).
*   **Method:** A **Function** that lives inside the class (e.g., `drive()`).

---

### 3. Function vs. Method

*   **Function:** A standalone tool. Like a hammer sitting on a table. Anyone can pick it up and use it on anything.
    *   `calculate_tax(price)`
*   **Method:** A tool that is **attached** to an object. Like the "Ice Maker" inside a specific refrigerator. You don't "pass the water" to the ice maker; it's already connected to the fridge's water line.
    *   `my_account.withdraw(500)`

---

### 4. How is a Class made? (The "init" and "self")

In Python, we use two special things that look weird at first:

1.  **`def __init__(self, ...)`**: This is the "Setup" function. It runs the very second you create a new object. It’s like the factory setting the car's color and model.
2.  **`self`**: This is the most important part. `self` means **"This specific object right here."** 
    *   If Alice withdraws money, `self.balance` refers to **Alice's** balance.
    *   If Bob withdraws money, `self.balance` refers to **Bob's** balance.

---

### 5. Let's see it in slow motion

Read this code carefully. I've added comments to explain exactly what is happening.

```python
# 1. This is the BLUEPRINT (The Class)
class BankAccount:
    def __init__(self, owner_name, starting_balance):
        # We attach the data to 'self' so the object "remembers" it
        self.owner = owner_name
        self.balance = starting_balance

    # This is a METHOD (An action this object can do)
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{self.owner} now has ${self.balance}")

# 2. This is how we use it (Creating INSTANCES)
alice_acc = BankAccount("Alice", 1000) # Created one 'house' from the blueprint
bob_acc = BankAccount("Bob", 50)       # Created a second 'house'

# 3. Calling METHODS
alice_acc.deposit(500)  # Only Alice's balance changes.
bob_acc.deposit(10)     # Only Bob's balance changes.
```

---

### Your "Slow-Down" Exercise

To make sure this clicks, I want you to build a very simple Class. We aren't going to do anything advanced. 

**The Scenario:** You are building a system for a Coffee Shop.

**Task:**
1.  Create a Class called `CoffeeOrder`.
2.  In the `__init__` method, take two arguments: `customer_name` and `coffee_type` (e.g., "Latte"). Save them to `self`.
3.  Add one more attribute in the `__init__` called `is_ready` and set it to `False` by default. (You don't need to pass this in as an argument; just set `self.is_ready = False`).
4.  Create a Method called `complete_order`. All it does is change `self.is_ready` to `True`.
5.  Create a Method called `get_status`. 
    *   If `self.is_ready` is `True`, return `"Your [coffee_type] is ready, [customer_name]!"`
    *   If `False`, return `"Still brewing..."`

**Try to write this out.** Don't worry about being perfect. Just try to get the `self` parts right.

**Follow-up Question:** 
In the `get_status` method, why do we use `self.customer_name` instead of just `customer_name`?
**Answer in 9slowdownexerice.py**




### One Last OOP Pillar: Inheritance (Sub-classes)

Before we leave OOP, you need to know about **Inheritance**. This is how we avoid writing the same code twice.

In a backend system, you might have a `User` class, but you also need an `Admin` class. An `Admin` **is a** `User`, but with extra powers.

```python
# The Parent Class
class User:
    def __init__(self, name):
        self.name = name
    
    def login(self):
        return f"{self.name} logged in."

# The Child Class (Inherits from User)
class Admin(User):
    def delete_everything(self):
        return "Database deleted! (Only admins can do this)"

# --- Usage ---
boss = Admin("The CEO")
print(boss.login())             # Admin gets 'login' for free!
print(boss.delete_everything()) # Admin has its own special powers
```

---

Slowing down to master **Inheritance** is a smart move. In backend engineering, if you don't understand inheritance, you will end up writing the same code 50 times, which makes your app a nightmare to maintain.

Inheritance is about the **"Is-A"** relationship. 
*   An `Admin` **is a** `User`.
*   A `StripePayment` **is a** `Payment`.
*   An `EmailNotification` **is a** `Notification`.

Let's look at the three levels of "Deep Inheritance" you need for professional Python work.

---

### 1. The `super()` Function (The Most Important Tool)
When a child class (like `Admin`) needs to do everything a parent class (`User`) does, **plus** a little more, we use `super()`. 

`super()` tells Python: *"Go run the logic from my parent first, then I'll add my extra stuff."*

**The Backend Example: User Roles**
```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        print("User initialized!")

class Admin(User):
    def __init__(self, username, email, access_level):
        # Instead of self.username = username (repeating code),
        # we call the parent's __init__
        super().__init__(username, email)
        
        # Then we add the admin-specific data
        self.access_level = access_level
        print("Admin access level set!")

boss = Admin("chief_dev", "boss@corp.com", 10)
```

### 2. Method Overriding
Sometimes, a child class needs to have the **same method name** as the parent, but it needs to behave differently.

**The Backend Example: Different API Responses**
```python
class BaseResponse:
    def send(self):
        return "Generic Response: 200 OK"

class ErrorResponse(BaseResponse):
    def send(self):
        # We 'override' the parent's send method with a specific version
        return "Error Response: 404 Not Found"

success = BaseResponse()
fail = ErrorResponse()

print(success.send()) # Generic Response: 200 OK
print(fail.send())    # Error Response: 404 Not Found
```

### 3. Abstract Logic (The "Template" Pattern)
In big backend projects, we often create a "Base" class that is just a template. It defines *what* methods must exist, but the child classes define *how* they work.

---

### Real-World Backend Example: Notification System

Imagine you are building a system that sends notifications to users. You want a consistent way to send them, whether it's via Email or SMS.

```python
class Notification:
    def __init__(self, recipient):
        self.recipient = recipient

    def send(self, message):
        # Every notification has a recipient, but 
        # 'send' will be defined by the specific type
        raise NotImplementedError("Subclasses must implement send()")

class EmailNotification(Notification):
    def send(self, message):
        return f"Sending Email to {self.recipient}: {message}"

class SMSNotification(Notification):
    def send(self, message):
        return f"Sending SMS to {self.recipient}: {message}"

# Now you can loop through any kind of notification and just call .send()
notifications = [
    EmailNotification("alice@test.com"),
    SMSNotification("+123456789")
]

for n in notifications:
    print(n.send("Hello!"))
```

---

### Your Coding Challenge: The Payment System

You are building a checkout system. You have a base `Payment` class, and you need to create specific payment methods.

**Task:**
1.  Create a class called `Payment`. 
    *   In `__init__`, take an `amount: float`.
    *   Create a method `process` that just returns a string: `"Processing $[amount]..."`.
2.  Create a class called `CreditCardPayment` that **inherits** from `Payment`.
    *   In `__init__`, take `amount` and `card_number: str`. 
    *   Use `super()` to handle the `amount`.
    *   **Override** the `process` method to return: `"Processing $[amount] via Credit Card [card_number]..."`.
3.  Create a class called `PayPalPayment` that **inherits** from `Payment`.
    *   In `__init__`, take `amount` and `email: str`.
    *   Use `super()` to handle the `amount`.
    *   **Override** the `process` method to return: `"Processing $[amount] via PayPal account [email]..."`.

**Test your code:**
Create one of each, put them in a list, and loop through the list calling `.process()` on each one.

```python
# TODO: Write your classes here

if __name__ == "__main__":
    payments = [
        CreditCardPayment(100.50, "1234-5678"),
        PayPalPayment(50.00, "user@test.com")
    ]
    # TODO: Loop and print process()
```

---

### 🧠 Senior Question:
If I have a variable `p = CreditCardPayment(100, "123")`, and I run `isinstance(p, Payment)`, will it be `True` or `False`? Why? 

**Answer in 10paymentsys.py**