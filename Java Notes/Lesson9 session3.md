# 📚 Session 3 — Java Keywords

## Learning Objectives

By the end of this session, you will be able to:

* Explain what a Java keyword is.
* Recognise the most commonly used keywords.
* Group keywords by their purpose instead of memorising a long list.
* Understand why Java has reserved keywords.
* Explain the role of `public`, `private`, `static`, `final`, `if`, `for`, `return`, and others.

---

# 1. What is a Java Keyword?

A **keyword** is a word that has a predefined meaning in the Java language.

Because Java already understands these words, **you cannot use them as names** for variables, methods, or classes.

For example:

```java
int if = 5;
```

❌ This will not compile because `if` is a keyword.

Likewise:

```java
String class = "Java";
```

❌ `class` is also a reserved keyword.

Think of keywords as **commands in Java's vocabulary**. They already have a specific meaning, so you cannot redefine them.

---

# 2. Why does Java have reserved keywords?

Imagine writing:

```java
if (age > 18) {
    ...
}
```

The compiler immediately knows that `if` starts a conditional statement.

Now imagine if programmers could rename it:

```java
banana (age > 18) {
    ...
}
```

Every program would invent its own language!

By reserving keywords, Java ensures that all programs follow the same grammar, making code easier to read and compile.

---

# 3. Don't Memorise 50+ Keywords

Java has many keywords, but beginners only use a small subset regularly.

We'll group them into categories.

---

# A. Access Modifiers

These control **who can access** a class, method, or variable.

## `public`

Accessible from anywhere.

```java
public class Main {
}
```

Think:

> "Everyone can use this."

---

## `private`

Accessible **only inside the same class**.

Example:

```java
private int age;
```

Think of a diary.

Only you can read it.

That's what `private` means.

---

## `protected`

Accessible within the same package and by subclasses.

We'll revisit this when we study inheritance.

For now, just know it exists between `public` and `private`.

---

# B. Class Keywords

## `class`

Defines a class.

```java
public class Car {
}
```

Remember:

A class is a **blueprint**.

You can create many objects from one class.

---

## `new`

Creates an object.

```java
String name = new String("Mike");
```

Another example:

```java
Scanner scanner = new Scanner(System.in);
```

Think:

> "`new` builds a new object."

---

# C. Method Keywords

## `static`

You struggled with this in Session 1, so let's reinforce it.

### Without `static`

The method belongs to an **object**.

```
Car object

↓

startEngine()
```

---

### With `static`

The method belongs to the **class itself**.

```
Math class

↓

Math.max()
```

No object is needed.

That's why:

```java
Math.sqrt(25);
```

works without creating a `Math` object.

Similarly, the JVM calls:

```java
public static void main(...)
```

without creating a `Main` object first.

---

## `void`

Means the method returns **nothing**.

```java
public static void greet() {

    System.out.println("Hello");

}
```

It performs an action but returns no value.

---

## `return`

Sends a value back to the caller.

Example:

```java
public static int add(int a, int b) {
    return a + b;
}
```

Here:

```java
return a + b;
```

gives the result back to whoever called the method.

---

# D. Primitive Type Keywords

You've already learned these.

```java
int
long
double
boolean
char
```

These are keywords because Java defines them directly.

---

# E. Decision Keywords

## `if`

Executes code only when a condition is true.

```java
if (age >= 18) {
    System.out.println("Adult");
}
```

---

## `else`

Runs when the `if` condition is false.

```java
if (age >= 18) {
    System.out.println("Adult");
} else {
    System.out.println("Minor");
}
```

---

## `switch`

Used for exact value matching.

```java
switch (day) {
    case 1:
        System.out.println("Monday");
        break;
    default:
        System.out.println("Unknown");
}
```

We'll study this in Session 6.

---

## `case`

Represents one possible value inside a `switch`.

---

## `default`

Runs if no `case` matches.

---

# F. Loop Keywords

## `for`

Repeats code a fixed number of times.

```java
for (int i = 1; i <= 5; i++) {
    System.out.println(i);
}
```

---

## `while`

Repeats while a condition remains true.

```java
while (running) {
    // keep running
}
```

---

## `break`

Stops the current loop or `switch`.

```java
break;
```

---

## `continue`

Skips the rest of the current iteration and moves to the next one.

```java
continue;
```

---

# G. Constants

## `final`

Makes something unchangeable.

Example:

```java
final double PI = 3.14159;
```

Trying to change it later:

```java
PI = 4;
```

❌ Compile-time error.

Think of `final` as:

> "This value is locked."

---

# H. Packages

## `import`

Brings another class into your program.

Example:

```java
import java.util.Scanner;
```

Without importing it, Java won't know what `Scanner` is.

---

## `package`

Groups related classes together.

Example:

```java
package com.mycompany.project;
```

You'll use this more as your projects grow.

---

# Common Beginner Mistakes

### Using a keyword as a variable name

```java
int class = 5;
```

❌ Invalid.

---

### Forgetting `return`

```java
public static int add(int a, int b) {

}
```

❌ Compile-time error because the method promises to return an `int` but returns nothing.

---

### Changing a `final` variable

```java
final int age = 25;

age = 30;
```

❌ Compile-time error.

---

# Keywords You'll Use Most Often

| Keyword                                    | Purpose                          |
| ------------------------------------------ | -------------------------------- |
| `public`                                   | Accessible from anywhere         |
| `private`                                  | Accessible only within the class |
| `class`                                    | Defines a class                  |
| `new`                                      | Creates an object                |
| `static`                                   | Belongs to the class             |
| `void`                                     | Returns nothing                  |
| `return`                                   | Sends a value back               |
| `int`, `double`, `boolean`, `char`, `long` | Primitive types                  |
| `if`                                       | Conditional execution            |
| `else`                                     | Alternative branch               |
| `for`                                      | Loop                             |
| `while`                                    | Loop                             |
| `switch`                                   | Multi-way selection              |
| `break`                                    | Exit a loop or `switch`          |
| `continue`                                 | Skip to the next loop iteration  |
| `final`                                    | Prevent changes                  |
| `import`                                   | Use classes from other packages  |

---

# Summary

You should now understand:

* ✅ What a Java keyword is.
* ✅ Why keywords are reserved.
* ✅ The main categories of keywords.
* ✅ The purpose of the most common keywords.
* ✅ Why grouping keywords is easier than memorising a list.

---

# Mini Quiz (Interview Style)

Answer these without looking back.

### 1. What is a Java keyword?

---

### 2. Why can't you name a variable `if` or `class`?

---

### 3. Explain the difference between:

* `public`
* `private`

---

### 4. What is the purpose of `static`?

---

### 5. What is the difference between `void` and `return`?

---

### 6. What does the `new` keyword do?

---

### 7. What is the purpose of `final`?

---

### 8. Which keyword would you use to:

a) create an object

b) define a class

c) repeat code

d) import another class

e) stop a loop immediately

---

## Engineer's Challenge

Instead of memorising keywords individually, explain **why Java needs keywords at all**.

Think about it from the compiler's perspective:

> How would the compiler know where a class starts, where a loop begins, or whether a method returns a value if keywords didn't exist?

This kind of reasoning is what distinguishes engineers from people who simply memorise syntax.


1) it is reserved word 
2) bc it is reserved 
3) public is where it is accessible everywhere and private is where it is accessible inside the class itself 
4) the purpose of static is to say that it belongs to that class
5) void is return nothing and return is returning sth 
6) it defineds sth new 
7) i dont know 
8) do it for me



You're doing well. I can see that you're **understanding the ideas**, but sometimes your answers are a little too short. In an interview, you'd want to add one more sentence explaining **why**. Let's go through them.

---

# 1. What is a Java keyword?

> **Your answer:** "it is reserved word"

### ✅ Score: 9/10

Correct.

A stronger interview answer would be:

> **A Java keyword is a reserved word with a predefined meaning in the Java language. It cannot be used as an identifier, such as a variable, method, or class name.**

---

# 2. Why can't you name a variable `if` or `class`?

> **Your answer:** "bc it is reserved"

### ✅ Score: 10/10

Correct.

To expand:

> Because the compiler already uses these words to understand Java's syntax. If programmers could reuse them as variable names, the compiler would not know what they mean.

---

# 3. Difference between `public` and `private`

> **Your answer:**
>
> "public is where it is accessible everywhere and private is where it is accessible inside the class itself"

### ✅ Score: 10/10

Excellent.

That's exactly what I wanted.

---

# 4. What is the purpose of `static`?

> **Your answer:**
>
> "the purpose of static is to say that it belongs to that class"

### ✅ Score: 10/10

Perfect.

That's much better than Session 1.

You've understood it.

---

# 5. Difference between `void` and `return`

> **Your answer:**
>
> "void is return nothing and return is returning sth"

### ✅ Score: 9.5/10

Correct.

Let's make it even clearer.

```java
public static void hello() {
    System.out.println("Hello");
}
```

This method performs an action.

It gives nothing back.

---

```java
public static int add(int a, int b) {
    return a + b;
}
```

Here:

```java
return a + b;
```

sends an integer back.

Think of `return` as:

> "Here is the result you asked for."

---

# 6. What does `new` do?

> **Your answer:**
>
> "it defineds sth new"

### ⚠️ Almost.

Not "defines."

It **creates** a new object.

Example:

```java
Scanner scanner = new Scanner(System.in);
```

Here,

```java
new Scanner(...)
```

creates a brand-new `Scanner` object.

So the interview answer is:

> The `new` keyword creates a new object in memory.

---

# 7. What is `final`?

You said:

> I don't know.

That's completely fine.

This is actually an important keyword.

Imagine this:

```java
final double PI = 3.14159;
```

Later:

```java
PI = 5;
```

Java says:

> ❌ No.

Why?

Because

```java
final
```

means

> This value cannot change after it has been assigned.

Think of it like writing with permanent marker instead of pencil.

You can read it.

You cannot overwrite it.

---

# 8. Let's do it together

### a) Create an object

```java
new
```

Example

```java
Scanner scanner = new Scanner(System.in);
```

---

### b) Define a class

```java
class
```

Example

```java
public class Car {
}
```

---

### c) Repeat code

There are several loop keywords, but the expected answer is

```java
for
```

Example

```java
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}
```

---

### d) Import another class

```java
import
```

Example

```java
import java.util.Scanner;
```

---

### e) Stop a loop immediately

```java
break
```

Example

```java
for (int i = 0; i < 10; i++) {

    if (i == 5) {
        break;
    }

}
```

The loop stops as soon as `i` becomes `5`.

---

# Engineer's Challenge

> **Why does Java need keywords?**

This is the most important question.

Imagine Java had **no keywords**.

Instead of:

```java
public class Main {

}
```

You could write:

```java
banana apple Main {

}
```

How would the compiler know:

* where a class begins?
* where a loop starts?
* whether a method returns a value?
* whether something is private or public?

It couldn't.

Keywords give Java a **grammar**, just as words like **if**, **while**, and **because** give English a grammar.

Without keywords, the compiler would have no consistent way to understand your program.

---

# Progress Check

You've now completed:

* ✅ Session 1 — Java Basics
* ✅ Session 2 — Variables & Primitive Types
* ✅ Session 3 — Java Keywords

Notice how the sessions build on each other:

```
Session 1
How Java works
        ↓
Session 2
What data Java stores
        ↓
Session 3
How Java describes code
        ↓
Session 4
How Java makes decisions (if / else)
```

You're building the foundations in the right order.

---

## C1 English upgrade

A few small improvements to your wording:

* ❌ "bc it is reserved"

  * ✅ "Because it is a reserved keyword."

* ❌ "it defineds sth new"

  * ✅ "It creates a new object."

* ❌ "void is return nothing"

  * ✅ "A `void` method does not return a value."

These are the kinds of phrases you'll hear and use in professional technical discussions.
