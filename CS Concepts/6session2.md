# 📚 Session 2 — Variables and Primitive Types

## Learning Objectives

By the end of this session, you will be able to:

* Explain what a variable is.
* Understand declaration vs initialisation.
* Know the difference between primitive and reference types.
* Use Java's most common primitive types.
* Print values to the console.
* Understand why Java requires explicit types.

---

# 1. What is a Variable?

Let's forget programming for a moment.

Imagine you have labelled storage boxes.

```
┌──────────────┐
│ Age          │
│ 23           │
└──────────────┘
```

Another one:

```
┌──────────────┐
│ Name         │
│ Mike         │
└──────────────┘
```

Each box has:

* a **name**
* a **value**

A **variable** is exactly that.

> A variable is a named location in memory used to store a value.

The computer remembers:

```
age → 23
```

instead of you remembering an actual memory address like:

```
0x7ffeab23...
```

---

# 2. Declaration vs Initialisation

These are two different concepts.

## Declaration

You're telling Java:

> "I want a variable of this type."

```java
int age;
```

Nothing is stored yet (for a local variable inside a method).

You have only declared it.

---

## Initialisation

Now you give it a value.

```java
age = 23;
```

Now the variable stores something.

---

## Declaration + Initialisation

Usually we combine both.

```java
int age = 23;
```

This is by far the most common form.

---

## Think like an engineer

Imagine you're opening a bank account.

Declaration:

```
Account exists.
```

Initialisation:

```
£500 deposited.
```

The account existed before money was added.

Variables work the same way.

---

# 3. Why Does Java Need the Type?

Suppose you write:

```java
int age = 23;
```

The compiler immediately knows:

* this is an integer
* it occupies 32 bits
* arithmetic is allowed
* strings are not allowed

Now imagine:

```java
age = "Mike";
```

Should Java allow this?

No.

The compiler already knows:

```
age
```

must always contain an integer.

That's static typing.

---

# 4. Primitive Types

Java has **8 primitive types**.

Think of primitives as the **basic building blocks** of data.

Unlike objects, they store simple values directly.

---

## `int`

Stores whole numbers.

```java
int age = 23;
```

Examples:

```java
int apples = 15;
int score = 100;
int temperature = -5;
```

---

## `long`

Used for very large whole numbers.

```java
long population = 8_000_000_000L;
```

Notice the `L`.

Without it, Java assumes an integer literal (`int`), which may be too small.

---

## `double`

Stores decimal numbers.

```java
double price = 9.99;
double pi = 3.14159;
```

---

## `boolean`

Stores only:

```java
true
false
```

Example:

```java
boolean isLoggedIn = true;
boolean hasPermission = false;
```

---

## `char`

Stores a **single character**.

```java
char grade = 'A';
```

Notice:

Single quotes:

```java
'A'
```

NOT

```java
"A"
```

because `"A"` is a `String`.

---

# Primitive Summary

| Type      | Stores              | Example       |
| --------- | ------------------- | ------------- |
| `int`     | Whole numbers       | `25`          |
| `long`    | Large whole numbers | `9000000000L` |
| `double`  | Decimal numbers     | `19.99`       |
| `boolean` | `true` or `false`   | `true`        |
| `char`    | One character       | `'A'`         |

---

# What About These?

You also read about:

```java
byte
short
float
```

You don't need them very often.

Professional Java developers mostly use:

* `int`
* `long`
* `double`
* `boolean`
* `char`

---

# 5. Primitive vs Reference Types

This is one of the biggest concepts in Java.

Let's compare.

## Primitive

```java
int age = 23;
```

Stores the value directly.

Think of it like:

```
age

23
```

---

## Reference

```java
String name = "Mike";
```

This does **not** directly store the text.

Instead, it stores a **reference** to a `String` object.

At this stage, think of a reference as **an address pointing to where the object lives in memory**.

```
name
  │
  ▼
"Mike"
```

We'll explore memory in more detail later.

---

## Why is `String` Not Primitive?

A primitive has a fixed size and a very simple representation.

A `String`:

* can have different lengths
* provides methods like `.length()`, `.toUpperCase()`, `.substring()`
* is an object with behaviour, not just a simple value

That's why it's a **reference type**.

---

# 6. Printing Values

You've already seen:

```java
System.out.println("Hello");
```

Now let's print variables.

```java
int age = 23;

System.out.println(age);
```

Output:

```
23
```

---

Print multiple variables:

```java
String name = "Mike";
int age = 23;

System.out.println(name);
System.out.println(age);
```

Output:

```
Mike
23
```

---

# 7. String Concatenation

You can combine text and variables with `+`.

```java
String name = "Mike";
int age = 23;

System.out.println("Name: " + name);
System.out.println("Age: " + age);
```

Output:

```
Name: Mike
Age: 23
```

---

# 8. Variable Naming

Follow Java conventions.

Good:

```java
int age;
double accountBalance;
boolean isLoggedIn;
char grade;
```

Bad:

```java
int A;
int x1;
int abc123;
```

Use **camelCase** for variable names.

---

# Common Beginner Mistakes

### ❌ Forgetting to initialise a local variable

```java
int age;

System.out.println(age);
```

Compile-time error:

```
Variable age might not have been initialized
```

---

### ❌ Wrong type

```java
int age = "23";
```

Compile-time error.

---

### ❌ Using double quotes for `char`

Wrong:

```java
char grade = "A";
```

Correct:

```java
char grade = 'A';
```

---

### ❌ Forgetting the `L` for large `long` values

```java
long population = 8000000000;
```

This may fail because the number is treated as an `int` literal.

Correct:

```java
long population = 8000000000L;
```

---

# Exercise 2.1 (Your Coursework)

Create a class like this:

```java
public class Main {

    public static void main(String[] args) {

        int age = 23;
        double height = 1.78;
        boolean isStudent = true;
        char grade = 'A';

        System.out.println(age);
        System.out.println(height);
        System.out.println(isStudent);
        System.out.println(grade);

    }

}
```

Then add comments explaining:

* `public`
* `static`
* `void`

---

# Summary

You now know:

* ✅ What a variable is.
* ✅ Declaration vs initialisation.
* ✅ Why Java needs explicit types.
* ✅ The five most common primitive types.
* ✅ The difference between primitive and reference types (at a high level).
* ✅ How to print variables.
* ✅ Common beginner mistakes.

---

# Mini Quiz

Try answering these **without looking back**:

1. What is the difference between **declaring** a variable and **initialising** it?
2. Why is Java called a **statically typed** language?
3. What is the difference between a **primitive type** and a **reference type**?
4. Why is `String` **not** a primitive type?
5. Which primitive type would you use for:

   * a person's age
   * the price of a product
   * whether a user is logged in
   * a student's grade (`A`, `B`, `C`)
   * the population of the Earth
6. What is wrong with each of these?

```java
int age = "25";
```

```java
char grade = "A";
```

```java
long distance = 5000000000;
```

Take your time. I won't just mark your answers—I’ll explain the reasoning behind them, just as we did in Session 1.
