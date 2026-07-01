# 📘 OOP (Object-Oriented Programming) in Java – Study Notes

## 🎯 What is OOP?

**Definition:**

Object-Oriented Programming (OOP) is a programming style where we organise code using **objects** that represent real-world things.

Instead of writing one long program, we create objects that contain:

* **Data (fields)**
* **Behaviour (methods)**

### 🧠 Example

A `Car` object has:

**Fields (state):**

```java
String model;
String color;
int speed;
```

**Methods (behaviour):**

```java
start();
stop();
increaseSpeed();
```

---

# The Five Main OOP Concepts

1. Classes
2. Objects
3. Abstraction
4. Encapsulation
5. Inheritance
6. Polymorphism

---

# 1. Classes

### Definition

A **class** is a blueprint for creating objects.

It defines:

* fields
* constructors
* methods

### Example

```java
public class Car {

    private String model;
    private int speed;

    public Car(String model) {
        this.model = model;
    }

    public void increaseSpeed() {
        speed++;
    }
}
```

### Think of it like

A class is the **blueprint** of a house.

You can build many houses from one blueprint.

---

# 2. Objects

### Definition

An **object** is an actual instance created from a class.

### Example

```java
Car car1 = new Car("BMW");
Car car2 = new Car("Audi");
```

Now you have two different objects.

Each stores its own data.

```
car1
model = BMW

car2
model = Audi
```

### Remember

Class = blueprint

Object = real thing built from blueprint

---

# 3. Abstraction

### Definition

Abstraction means:

> Hide unnecessary complexity and show only what users need.

Users should know **how to use** something, not **how it works internally**.

### Example

Driving a car.

You press

```
Accelerator
Brake
Steering wheel
```

You don't need to understand how the engine works.

---

### Java uses:

* Abstract classes
* Interfaces

to achieve abstraction.

---

# 4. Encapsulation

### Definition

Encapsulation means:

> Protect an object's data by making fields private and providing controlled access through methods.

### Example

```java
private int speed;
```

Instead of

```java
car.speed = 100;
```

we do

```java
car.setSpeed(100);
```

or

```java
int speed = car.getSpeed();
```

### Why?

Because the object controls how its data changes.

Example:

```java
if(speed >= 0){
    this.speed = speed;
}
```

This prevents invalid values.

---

# 5. Inheritance

### Definition

Inheritance allows one class to reuse another class's code.

We say:

Child class **extends** Parent class.

---

### Example

```
Vehicle
```

↓

```
Car
```

↓

```
SportsCar
```

---

### Code

```java
class Vehicle{

    public void start(){

    }

}
```

```java
class Car extends Vehicle{

}
```

Car automatically gets

```
start()
```

without writing it again.

---

### Relationship

Inheritance creates an

**IS-A**

relationship.

```
Car IS-A Vehicle
```

```
Dog IS-A Animal
```

---

### Benefits

* Code reuse
* Less duplication
* Easier maintenance

---

### Method Overriding

Child classes can replace parent behaviour.

Parent

```java
public void honk(){

}
```

Child

```java
@Override
public void honk(){

}
```

Now the child uses its own implementation.

---

# 6. Polymorphism

### Definition

Polymorphism means

> One method name can behave differently depending on the object or parameters.

There are **two types**.

---

# A. Compile-time Polymorphism (Method Overloading)

Same method name

Different parameters

Example

```java
read()
```

```java
read(int limit)
```

```java
read(int start, int end)
```

Same name

Different inputs

Different behaviour

---

# B. Runtime Polymorphism (Method Overriding)

Parent

```java
public String getFileInfo(){

    return "Generic File";

}
```

Child

```java
@Override
public String getFileInfo(){

    return "Image File";

}
```

Same method

Different implementation.

Java decides which version to run while the program is running.

---

# Quick Comparison

| Concept       | Simple Definition                 | Example                  |
| ------------- | --------------------------------- | ------------------------ |
| Class         | Blueprint                         | `Car`                    |
| Object        | Instance of a class               | `new Car()`              |
| Abstraction   | Hide complexity                   | Driving a car            |
| Encapsulation | Protect data using private fields | Getters & setters        |
| Inheritance   | Reuse code from another class     | `Car extends Vehicle`    |
| Polymorphism  | One method, different behaviour   | Overloading & overriding |

---

# Relationships to Remember

```
Class
   ↓
creates
   ↓
Object
```

```
Encapsulation
↓

Protects object data
```

```
Inheritance
↓

Reuses code
```

```
Polymorphism
↓

Changes behaviour
```

```
Abstraction
↓

Hides complexity
```

---

# Revision Cheat Sheet

✅ **Class** = Blueprint

✅ **Object** = Instance of a class

✅ **Constructor** = Creates and initialises objects

✅ **Field** = Stores object data

✅ **Method** = Defines object behaviour

✅ **Encapsulation** = Private fields + getters/setters

✅ **Abstraction** = Hide implementation details

✅ **Inheritance** = Child inherits from parent (`extends`)

✅ **Method Overloading** = Same method name, different parameters (compile-time polymorphism)

✅ **Method Overriding** = Child replaces parent's method (runtime polymorphism)

---

## Where you are now

Based on what we've covered together, you already understand:

* ✅ Classes and objects
* ✅ Constructors
* ✅ Constructor overloading
* ✅ Constructor chaining
* ✅ Getters and setters
* ✅ `toString()`
* ✅ Encapsulation
* ✅ Reference behaviour

The next concepts to learn in depth are:

1. **Inheritance (`extends`)**
2. **Method overriding (`@Override`)**
3. **Polymorphism**
4. **Abstract classes**
5. **Interfaces**