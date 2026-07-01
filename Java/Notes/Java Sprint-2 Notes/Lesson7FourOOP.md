# Object-Oriented Programming (OOP) in Java

## 1. What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that organises software around **objects** rather than functions.

An object combines:

* **Data (fields/attributes)** → what the object knows
* **Behaviour (methods)** → what the object can do

### Why use OOP?

* Improves code reusability
* Makes code easier to maintain
* Makes large programs easier to organise
* Models real-world objects naturally

---

# 2. Class

## Definition

A **class** is a blueprint or template used to create objects.

It describes:

* what data an object has (fields)
* what actions it can perform (methods)

Think of it like:

> **Blueprint → House**
>
> One blueprint can create many different houses.

In Java:

```java
public class Car {

    private String type;
    private String model;
    private String colour;
    private int speed;

    public Car(String type, String model, String colour) {
        this.type = type;
        this.model = model;
        this.colour = colour;
    }

    public int increaseSpeed(int increment) {
        speed += increment;
        return speed;
    }
}
```

### Parts of a class

| Part        | Purpose           |
| ----------- | ----------------- |
| Fields      | Store data        |
| Constructor | Creates an object |
| Methods     | Define behaviour  |

---

# 3. Object

## Definition

An **object** is a real instance of a class.

The class is only a design.

The object is the actual thing created from that design.

Example:

```java
Car veyron = new Car("Bugatti", "Veyron", "Crimson");
Car corvette = new Car("Chevrolet", "Corvette", "Black");
```

Here:

* `Car` → class
* `veyron` → object
* `corvette` → object

Each object has its own data.

Example:

```
Car (Blueprint)

        ↓

Object 1
Type: Bugatti
Model: Veyron
Colour: Crimson

Object 2
Type: Chevrolet
Model: Corvette
Colour: Black
```

---

# 4. Constructor

## Definition

A constructor is a special method used to create an object.

It runs automatically whenever `new` is used.

Example:

```java
public Car(String type, String model, String colour) {
    this.type = type;
    this.model = model;
    this.colour = colour;
}
```

Called by:

```java
Car car = new Car("Toyota", "Corolla", "White");
```

A class can have multiple constructors (constructor overloading).

---

# 5. Abstraction

## Definition

Abstraction means:

> Hide unnecessary implementation details and show only what the user needs.

Users interact with **what** something does, not **how** it works.

Example:

When driving a car you use:

* steering wheel
* accelerator
* brake

You don't need to know how the engine works.

The engine is abstracted away.

### Java uses abstraction through:

* Interfaces
* Abstract classes

Goal:

```
Hide complexity

↓

Provide a simple interface
```

---

# 6. Encapsulation

## Definition

Encapsulation means protecting an object's data by hiding it from direct access.

Usually:

* fields → private
* methods → public

Example:

```java
public class Car {

    private int speed;

    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }
}
```

Instead of:

❌

```java
car.speed = 100;
```

We use:

```java
car.setSpeed(100);
```

### Why?

Because the class controls how data changes.

Example:

```java
public void setSpeed(int speed){

    if(speed >= 0){
        this.speed = speed;
    }
}
```

Now negative speeds cannot be set.

---

# 7. Inheritance

## Definition

Inheritance allows one class to reuse another class's code.

The child class inherits fields and methods from the parent.

Syntax:

```java
class Car extends Vehicle
```

Meaning:

```
Vehicle

↓

Car
```

Car automatically gets:

* fields
* methods

from Vehicle.

---

## Parent class

```java
public class Vehicle {

    private int wheels;
    private String model;

    public void start() {}

    public void stop() {}

    public void honk() {}
}
```

---

## Child class

```java
public class Car extends Vehicle {

    private int numberOfGears;

    public void openDoors() {}
}
```

Car now has:

Inherited:

* start()
* stop()
* honk()

Own:

* openDoors()

---

## Multilevel inheritance

```
Vehicle

↓

Car

↓

ArmouredCar
```

Example:

```java
public class ArmouredCar extends Car {

    private boolean bulletProofWindows;

    public void remoteStartCar(){}
}
```

ArmouredCar inherits everything from:

* Car
* Vehicle

---

## IS-A Relationship

Inheritance represents an IS-A relationship.

Examples:

```
Car IS-A Vehicle

Dog IS-An Animal

Cat IS-An Animal
```

---

# 8. Method Overriding

A child class can replace the parent's implementation.

Parent:

```java
public void honk() {
    // default honk
}
```

Child:

```java
@Override
public void honk() {
    // car-specific honk
}
```

The method name stays the same.

The implementation changes.

This is **runtime polymorphism**.

---

# 9. Polymorphism

## Definition

Polymorphism means:

> One interface, many forms.

The same method name can behave differently.

There are two types.

---

# A. Compile-time Polymorphism (Method Overloading)

Same method name.

Different parameters.

Example:

```java
read()

read(int limit)

read(int start, int stop)
```

All methods are called `read()`.

Java decides which one to call during compilation.

Example:

```java
file.read();

file.read(100);

file.read(10,50);
```

---

# B. Runtime Polymorphism (Method Overriding)

Parent:

```java
public String getFileInfo(){
    return "Generic File";
}
```

Child:

```java
@Override
public String getFileInfo(){
    return "Image File";
}
```

Example:

```java
GenericFile file = new ImageFile();

System.out.println(file.getFileInfo());
```

Output:

```
Image File
```

Although the variable type is `GenericFile`, Java executes the overridden method in `ImageFile`.

---

# 10. Relationship Between the OOP Concepts

```
Class
   │
   ▼
Creates
   │
Object
   │
   ├────────── Encapsulation
   │          Protects data
   │
   ├────────── Abstraction
   │          Hides complexity
   │
   ├────────── Inheritance
   │          Reuses code
   │
   └────────── Polymorphism
              Same interface,
              different behaviour
```

---

# 11. Summary Table

| Concept            | Purpose                           | Key Keyword                 |
| ------------------ | --------------------------------- | --------------------------- |
| Class              | Blueprint for objects             | `class`                     |
| Object             | Instance of a class               | `new`                       |
| Constructor        | Creates objects                   | Same name as class          |
| Abstraction        | Hide implementation details       | `abstract`, `interface`     |
| Encapsulation      | Protect internal data             | `private`, getters, setters |
| Inheritance        | Reuse code from another class     | `extends`                   |
| Method Overriding  | Replace parent behaviour          | `@Override`                 |
| Method Overloading | Same method, different parameters | Multiple method signatures  |
| Polymorphism       | One interface, many behaviours    | Overloading & overriding    |

---

## Key Takeaways

* A **class** is a blueprint; an **object** is an instance of that blueprint.
* A **constructor** initialises an object when it is created.
* **Abstraction** hides complexity and exposes only the necessary interface.
* **Encapsulation** protects an object's internal state by restricting direct access to its fields.
* **Inheritance** enables code reuse by allowing a child class to inherit from a parent class.
* **Method overriding** lets a child class provide its own implementation of a parent method.
* **Method overloading** allows multiple methods with the same name but different parameter lists.
* **Polymorphism** allows the same method call to produce different behaviour depending on the object involved.




# Java Access Modifiers – Summary

## What are Access Modifiers?

Access modifiers control **where classes, fields, methods, and constructors can be accessed from**.

Java has **four** access modifiers:

1. `public`
2. `protected`
3. `default` (package-private, no keyword)
4. `private`

> **Important:** A **top-level class** can only be `public` or **default**. It **cannot** be `private` or `protected`.

---

# 1. `public`

## Definition

The **least restrictive** access modifier.

A `public` member can be accessed from:

* The same class
* The same package
* Subclasses
* Any other class in any package

### Use when

The member is part of your application's **public API** and should be accessible everywhere.

Example:

```java
public class Car {

    public void start() {

    }

}
```

---

# 2. `private`

## Definition

The **most restrictive** access modifier.

A `private` member can only be accessed **within the same class**.

### Use when

You want to hide implementation details and protect data (**encapsulation**).

Example:

```java
public class Car {

    private int speed;

}
```

Only methods inside `Car` can directly access `speed`.

---

# 3. `protected`

## Definition

A `protected` member can be accessed by:

* The same class
* Classes in the same package
* Subclasses (even if they are in different packages)

### Use when

You want subclasses to inherit and use the member without making it public.

Example:

```java
protected void startEngine() {

}
```

---

# 4. `default` (Package-Private)

## Definition

If no access modifier is specified, Java uses the **default** (package-private) access level.

A package-private member can be accessed by:

* The same class
* Other classes in the same package

It **cannot** be accessed from classes in different packages.

Example:

```java
class Car {

    void drive() {

    }

}
```

No keyword is used.

---

# Access Modifier Comparison

| Modifier    | Same Class | Same Package | Subclass | Other Packages |
| ----------- | :--------: | :----------: | :------: | :------------: |
| `public`    |      ✅     |       ✅      |     ✅    |        ✅       |
| `protected` |      ✅     |       ✅      |     ✅    |       ❌*       |
| `default`   |      ✅     |       ✅      |     ❌    |        ❌       |
| `private`   |      ✅     |       ❌      |     ❌    |        ❌       |

> **Note:** `protected` members are accessible to subclasses in other packages, but **not** to unrelated classes in those packages.

---

# Canonical Order of Modifiers

Although Java doesn't require a specific order, the **Java Language Specification (JLS)** recommends a standard order for consistency and readability.

## Fields

```java
@Annotation
private static final long ID = 1;
```

Recommended order:

1. Annotation
2. Access modifier (`public`, `protected`, `private`)
3. `static`
4. `final`
5. `transient`
6. `volatile`

---

## Classes

Recommended order:

1. Annotation
2. Access modifier
3. `abstract`
4. `static`
5. `final`
6. `strictfp`

---

## Methods

Recommended order:

1. Annotation
2. Access modifier
3. `abstract`
4. `static`
5. `final`
6. `synchronized`
7. `native`
8. `strictfp`

> Not all modifiers can be combined. For example, `public`, `protected`, and `private` are mutually exclusive—you can only choose one access modifier.

---

# Best Practices

* Use the **most restrictive access modifier** that still allows your code to work.
* Make fields `private` by default to support **encapsulation**.
* Use `protected` only when subclasses need access.
* Use `default` when access should be limited to classes within the same package.
* Use `public` only for members that are intended to be part of the public API.

---

# Key Takeaways

* Java provides **four access modifiers**: `public`, `protected`, `default` (package-private), and `private`.
* **Top-level classes** can only be `public` or `default`.
* `private` provides the highest level of encapsulation by restricting access to the same class.
* `protected` extends package-private access by also allowing access from subclasses, even across packages.
* The JLS recommends a **canonical order** for modifiers to improve consistency and readability, although Java does not enforce it.







---

# Encapsulation vs Information Hiding

## The Short Answer

**Encapsulation** is about **organising code**.

**Information hiding** is about **protecting data**.

You almost always use **information hiding together with encapsulation**, but they are **not exactly the same thing**.

---

# Imagine a Car

Think about a car.

## Encapsulation

A car groups together:

* engine
* steering
* brakes
* gearbox

into **one object**.

Everything related to driving the car is contained inside the car.

This is **encapsulation**.

---

## Information Hiding

When you drive the car:

You can

* start it
* stop it
* steer it

But you **cannot directly touch**:

* the pistons
* fuel injectors
* gearbox

Those internal parts are hidden.

This is **information hiding**.

---

# Definition of Encapsulation

Encapsulation means:

> **Bundling data and the methods that operate on that data into one class.**

Instead of storing data in one class and writing functions in another class, we keep them together.

---

## Without Encapsulation

Imagine this class:

```java
class Book {

    public String author;
    public int isbn;

}
```

Another class performs the work:

```java
class BookDetails {

    public String getDetails(Book book) {

        return book.author + " " + book.isbn;

    }

}
```

The data is here:

```
Book
```

The behaviour is somewhere else:

```
BookDetails
```

This isn't modular.

---

## With Encapsulation

Instead:

```java
class Book {

    public String author;
    public int isbn;

    public String getBookDetails() {

        return author + " " + isbn;

    }

}
```

Now

```
Book

contains

Data
+
Behaviour
```

Everything belongs together.

This is encapsulation.

---

# Important Point

Notice something.

The fields are still

```java
public String author;
```

Anyone can still change them.

```java
book.author = "Someone Else";
```

So...

The class **is encapsulated**.

But the data **is not protected**.

---

# Information Hiding

Information hiding means

> **Prevent direct access to an object's internal data.**

Usually we do this using

```java
private
```

Example

```java
class Book {

    private String author;
    private int isbn;

}
```

Now this is illegal:

```java
book.author = "John";
```

Java says:

```
Cannot access private field.
```

Instead we provide methods.

```java
public String getAuthor() {

    return author;

}

public void setAuthor(String author) {

    this.author = author;

}
```

Now the object controls access to its own data.

---

# Why is this useful?

Suppose ISBN should never be negative.

Without information hiding:

```java
book.isbn = -50;
```

Nothing stops this.

With information hiding:

```java
public void setIsbn(int isbn) {

    if(isbn < 0){

        throw new IllegalArgumentException();

    }

    this.isbn = isbn;

}
```

Now invalid data cannot enter the object.

The object protects itself.

---

# Think of it Like a Bank

Imagine your bank account.

Without information hiding

You could write

```
Balance = £1,000,000
```

Obviously that would be terrible.

Instead

The bank gives you methods.

```
deposit()

withdraw()

getBalance()
```

You cannot directly modify

```
balance
```

That's information hiding.

---

# Relationship Between the Two

```text
Encapsulation

Bundles

Data
+
Methods

↓

Information Hiding

Protects the data
```

Information hiding builds on encapsulation.

You first bundle everything together.

Then you decide which parts should remain hidden.

---

# Can You Have Encapsulation Without Information Hiding?

Yes.

Example

```java
class Book {

    public String author;

    public void printBook() {

        System.out.println(author);

    }

}
```

Data and methods are together.

So the class is encapsulated.

But anyone can still change

```java
author
```

Therefore

It is **not** information hiding.

---

# Can You Have Information Hiding Without Encapsulation?

Practically speaking, no.

Information hiding is normally achieved **inside an encapsulated class**.

---

# Main Differences

| Encapsulation                                       | Information Hiding                                                     |
| --------------------------------------------------- | ---------------------------------------------------------------------- |
| Bundles data and methods into one class             | Protects the object's internal data                                    |
| Focuses on organising code                          | Focuses on restricting access                                          |
| Improves modularity                                 | Improves security and robustness                                       |
| Can use `public`, `protected`, or `private` members | Typically uses `private` fields with controlled access through methods |
| Answers **"How should related code be organised?"** | Answers **"What should other classes be allowed to access?"**          |

---

# Real-World Analogy

Imagine a television.

### Encapsulation

Everything needed to make the television work is inside one device.

* Screen
* Speakers
* Circuit board
* Power supply

They are bundled together.

---

### Information Hiding

The user only sees:

* Power button
* Volume controls
* Channel buttons

The electrical circuits and internal components are hidden.

---

# Easy Way to Remember

**Encapsulation = Bundle**

> Put related **data and behaviour** together in one class.

**Information Hiding = Protect**

> Hide the implementation and protect the object's internal data from direct access.

A useful phrase to remember is:

> **Encapsulation organises an object; information hiding protects it.**

