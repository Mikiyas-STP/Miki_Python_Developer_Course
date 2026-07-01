## What is OOP?

**Object-Oriented Programming (OOP)** is a programming paradigm (a way of writing programs) where you organise code into **objects**.

An **object** combines:

* **Data (state)** → what it knows (fields)
* **Behaviour** → what it can do (methods)

### Example

A `BankAccount` object has:

**State:**

* accountNumber
* balance
* ownerName

**Behaviour:**

* deposit()
* withdraw()
* checkBalance()

Instead of writing separate functions and variables, OOP groups related data and behaviour together.

---

## Why is Java an OOP Language?

Java is considered an OOP language because almost everything is built around **classes and objects**.

For example:

```java
class BankAccount {
    private double balance;

    public void deposit(double amount) {
        balance += amount;
    }
}
```

Here:

* `BankAccount` is a **class**
* `balance` is the object's **state**
* `deposit()` is the object's **behaviour**

When you create:

```java
BankAccount account = new BankAccount();
```

you're creating an **object** from the class.

Java also supports the four core principles of OOP:

1. **Encapsulation** – hide data and control access.
2. **Abstraction** – hide unnecessary implementation details.
3. **Inheritance** – create new classes based on existing ones.
4. **Polymorphism** – allow different objects to be used through a common interface.

These are the defining features of object-oriented programming.

---

## Advantages of OOP

### 1. Better Organisation

Related data and behaviour stay together.

Instead of scattered variables and functions, everything belongs to the object it represents.

---

### 2. Code Reuse

You can reuse existing classes through inheritance or composition instead of rewriting code.

---

### 3. Easier Maintenance

Each class has a single responsibility.

If something changes in `BankAccount`, you usually only modify that class.

---

### 4. Better Security

Private fields prevent other parts of the program from changing important data directly.

Example:

```java
private double balance;
```

Instead of:

```java
account.balance = -1000;
```

users must call:

```java
account.withdraw(100);
```

where you can validate the operation.

---

### 5. Easier to Extend

You can add new features by creating new classes without changing existing code too much.

---

## Advantages of OOP for Backend Development

Backend systems model **real-world business concepts**, and OOP maps naturally to those concepts.

For example, in an online shop you might have:

* `User`
* `Product`
* `Order`
* `ShoppingCart`
* `Payment`

Each becomes its own class with its own data and behaviour.

Example:

```text
User
 ├── name
 ├── email
 └── login()

Order
 ├── items
 ├── total
 └── calculateTotal()

Payment
 ├── amount
 └── processPayment()
```

This makes the codebase easier to understand because it reflects the business domain.

### Other backend benefits

* **Maintainability:** Large projects can be split into small, focused classes.
* **Scalability:** New features are easier to add without rewriting existing code.
* **Team collaboration:** Different developers can work on different classes or modules with fewer conflicts.
* **Reliability:** Encapsulation helps prevent invalid data and reduces bugs.
* **Testing:** Individual classes are easier to unit test in isolation.

---

## In One Sentence

**OOP is a way of organising software by modelling real-world entities as objects that combine data and behaviour. Java is designed around this model, making it well suited for building large, maintainable, scalable backend applications where business concepts naturally map to classes and objects.**
