
# 📚 Lesson 2 – Method Structure (Based on Baeldung)

## 🎯 Learning Objectives

By the end of this lesson, you should be able to:

* Identify all six parts of a Java method.
* Explain the purpose of each part.
* Know which parts are optional.
* Read a method from left to right.

---

## What Baeldung Says

Baeldung states that a Java method consists of **six parts**:

1. Access modifier *(optional)*
2. Return type
3. Method identifier
4. Parameter list *(optional)*
5. Exception list *(optional)*
6. Method body

We'll use this method throughout the lesson:

```java
public static String greetUser(String name) throws IOException {
    return "Hello, " + name;
}
```

Don't worry if you don't recognise every keyword yet. By the end of this lesson, you'll understand what each part is for.

---

## The Six Parts at a Glance

| Part              | Example              | Required? |
| ----------------- | -------------------- | --------- |
| Access modifier   | `public`             | No        |
| Return type       | `String`             | Yes       |
| Method identifier | `greetUser`          | Yes       |
| Parameter list    | `(String name)`      | No        |
| Exception list    | `throws IOException` | No        |
| Method body       | `{ ... }`            | Yes       |

One thing to notice immediately is that **not every part is required**.

Some methods won't have parameters.

Some won't throw exceptions.

Some won't specify an access modifier.

But **every method must have**:

* a return type (`void` counts as a return type),
* a method name,
* and a body.

We'll explore each part one at a time in the next sections of Lesson 2, starting with **access modifiers**, exactly in the order your Baeldung resource presents them. This keeps us aligned with your course while making each concept easier to digest before moving on.



---

# 📚 Lesson 2 – Method Structure

## Part 1 – Access Modifier

Baeldung says:

> **Access modifier: optionally we can specify from where in the code one can access the method.**

Let's unpack that sentence.

---

# What is an Access Modifier?

An **access modifier** tells Java:

> **Who is allowed to use this method?**

Think of it as setting permissions.

Imagine you have a room in your house.

You can decide who is allowed to enter.

```
🚪 Room

Everyone        ✅
Family only     ✅
Only me         ✅
Nobody          ❌
```

An access modifier does the same thing for methods.

It controls **who can call the method**.

---

# Is it Required?

No.

Baeldung specifically says it is **optional**.

If you don't write one:

```java
void sayHello() {

}
```

Java gives the method **default (package-private)** access.

You don't need to understand package-private yet. The important thing from the resource is:

> Access modifiers are optional.

---

# Common Access Modifiers

Baeldung mentions four:

| Modifier    | Meaning                               |
| ----------- | ------------------------------------- |
| `public`    | Accessible from anywhere              |
| `protected` | Accessible in certain related classes |
| `private`   | Accessible only inside the same class |
| *(default)* | Accessible within the same package    |

For now, just recognise these names. Your exercises will mainly use `public` and `private`.

---

# Example 1

```java
public static void sayHello() {

}
```

Here:

```
public
```

is the access modifier.

---

# Example 2

```java
private static int calculateSum(int a, int b) {

}
```

Here:

```
private
```

is the access modifier.

---

# Example 3

```java
static void printMessage() {

}
```

Notice something.

There is **no** access modifier.

This is still valid Java.

That is why Baeldung says the access modifier is optional.

---

# Check Your Understanding

Identify the access modifier.

### Example A

```java
public void login() {

}
```

Answer:

```
public
```

---

### Example B

```java
private int calculateAge() {

}
```

Answer:

```
private
```

---

### Example C

```java
void print() {

}
```

Answer:

No access modifier has been written.

---

# Baeldung's Note About `static`

Immediately after explaining access modifiers, Baeldung introduces something else.

It says:

> A method can also include the `static` keyword before or after the access modifier.

Example:

```java
public static void sayHello() {

}
```

or

```java
static public void sayHello() {

}
```

Both are valid Java.

However,

Baeldung also notes that **`public static` is the common style**, and that's the style you'll see almost everywhere.

---

# What Does `static` Mean?

Baeldung says:

> The method belongs to the class and not to the instances.

This is exactly the same explanation you saw in W3Schools.

At this stage, that's enough.

You'll study classes and objects later, so we won't go beyond what the resource says.

---

# Static vs Non-static

Baeldung compares two kinds of methods.

## Static method

```java
public static void print() {

}
```

Baeldung says:

> We can call this method **without creating an object**.

---

## Instance method

```java
public void print() {

}
```

Baeldung says:

> This method may only be invoked on an instance of the class.

Again, don't worry about objects yet. The key takeaway from the resource is:

* `static` methods can be called directly using the class name.
* Methods without `static` require an object.

We'll revisit this when we study classes.

---

# Memory Note (from Baeldung)

Baeldung briefly mentions:

> Static methods are loaded into memory once during class loading.

You do **not** need to memorise this.

It's simply explaining one reason why static methods can be more memory-efficient.

Since your course hasn't introduced memory management yet, it's enough to know that Baeldung mentions it as background information.

---

# Summary

From this section of the resource:

* An **access modifier** controls who can access a method.
* Access modifiers are **optional**.
* The four access modifiers are:

  * `public`
  * `protected`
  * `private`
  * default (package-private)
* A method may also include the `static` keyword.
* `static` means the method belongs to the class rather than an object.

---

# 📝 Quick Check

Without looking back, answer these:

1. Is an access modifier required for every method?

2. Name the four access modifiers mentioned by Baeldung.

3. According to Baeldung, what does the `static` keyword mean?

4. Which is the common style?

```java
static public void print()
```

or

```java
public static void print()
```

---

## Next Part

We'll continue with **Return Type**, where Baeldung explains:

* What a return type is.
* Why `void` is a return type.
* Why methods with a return type must use `return`.
* What happens after a `return` statement executes.

This section is especially important because it directly prepares you for **Exercise 3.1 (`greetUser`)** and **Exercise 3.2 (`calculateSum`)**, where you'll write methods that return values.











Great! We're continuing **Lesson 2** in the same style, following only your Baeldung resource.

---

# 📚 Lesson 2 – Part 2: Return Type

Baeldung says:

> **Return type: the type of the value returned by the method, if any.**

Let's understand what that means.

---

# What is a Return Type?

A **return type** tells Java:

> **What kind of value this method gives back after it finishes.**

Think of calling a method like asking someone to do a task.

Sometimes they only perform the task.

Sometimes they perform the task **and give you something back**.

For example:

```
You: "Please print my homework."

Friend: "Done."

You don't receive anything back.
```

But:

```
You: "What is 5 + 3?"

Friend: "8"

Now you receive a value back.
```

Methods work the same way.

---

# Two Possibilities

A method can either:

### 1. Return a value

Example:

```java
static int add(int a, int b) {
    return a + b;
}
```

This method gives back an integer.

---

### 2. Return nothing

Example:

```java
static void printHello() {
    System.out.println("Hello");
}
```

This method only prints a message.

It gives nothing back.

---

# The Return Type Appears Before the Method Name

Look carefully.

```java
public static String greetUser(String name) {
```

Break it down:

```
public      ← access modifier
static      ← keyword
String      ← return type
greetUser   ← method name
```

The return type is **always written immediately before the method name**.

---

# Common Return Types

Baeldung says a method can return:

* a primitive value
* an object reference
* nothing (`void`)

Here are some examples:

| Return Type | Returns           |
| ----------- | ----------------- |
| `int`       | whole number      |
| `double`    | decimal number    |
| `boolean`   | `true` or `false` |
| `char`      | single character  |
| `String`    | text              |
| `void`      | nothing           |

---

# Example 1 – Returning an Integer

```java
public static int calculateSum(int a, int b) {
    return a + b;
}
```

Reading it:

* access modifier → `public`
* keyword → `static`
* return type → `int`
* method name → `calculateSum`

When called:

```java
int result = calculateSum(4, 6);
```

The method returns:

```
10
```

---

# Example 2 – Returning a String

```java
public static String greetUser(String name) {
    return "Hello, " + name;
}
```

Calling:

```java
String message = greetUser("Alice");
```

The returned value is:

```
Hello, Alice
```

---

# Example 3 – Returning Nothing

```java
public static void greet() {
    System.out.println("Hello");
}
```

This method only performs an action.

Nothing comes back.

---

# The `return` Statement

Baeldung says:

> **If we declare a return type, then we have to specify a return statement in the method body.**

This is an important rule.

Suppose we write:

```java
public static int add(int a, int b) {

}
```

Java will produce a compilation error.

Why?

Because we promised to return an `int`, but we never actually returned one.

The correct version is:

```java
public static int add(int a, int b) {
    return a + b;
}
```

The `return` statement sends the value back to whoever called the method.

---

# What Happens After `return`?

Baeldung also says:

> **Once the return statement has been executed, the execution of the method body will be finished.**

Let's see an example.

```java
public static int multiply(int a, int b) {

    return a * b;

    System.out.println("Finished");

}
```

What happens?

The `return` statement ends the method immediately.

The line:

```java
System.out.println("Finished");
```

will never run.

In fact, Java won't even compile this code because that line is **unreachable**.

---

# Does a `void` Method Need `return`?

Baeldung says:

> **A void method doesn't return any value.**

Example:

```java
public static void welcome() {
    System.out.println("Welcome");
}
```

No `return` statement is needed because the method doesn't promise to return anything.

---

# Comparing `void` and `String`

### `void`

```java
public static void sayHello() {
    System.out.println("Hello");
}
```

What happens?

```
Prints:
Hello

Returns:
Nothing
```

---

### `String`

```java
public static String sayHello() {
    return "Hello";
}
```

What happens?

```
Prints:
Nothing

Returns:
"Hello"
```

Notice the difference:

* `System.out.println()` displays something on the screen.
* `return` sends a value back to the caller.

These are **not** the same thing.

---

# Summary

From Baeldung:

* Every method has a return type.
* The return type tells Java what kind of value the method returns.
* `void` means the method returns nothing.
* If a method has a return type such as `int` or `String`, it **must** contain a `return` statement.
* When the `return` statement executes, the method finishes immediately.

---

# 📝 Quick Check

### Question 1

What is the return type here?

```java
public static boolean isLoggedIn() {

}
```

---

### Question 2

What does `void` mean?

---

### Question 3

True or False?

A method with return type `int` can finish without a `return` statement.

---

### Question 4

What happens after Java executes a `return` statement?

---

### Question 5

Identify the return type:

```java
public static String getName() {

}
```

---

## Before We Move On

There's one subtle point in this section that often confuses beginners:

> **Printing a value is not the same as returning a value.**

For example:

```java
public static void showAge() {
    System.out.println(25);
}
```

This **prints** `25` to the console, but the method returns **nothing** because its return type is `void`.

In contrast:

```java
public static int getAge() {
    return 25;
}
```

This method doesn't print anything. Instead, it **returns** the value `25` so the code that called it can use it.

Understanding this distinction will make the upcoming exercises (`greetUser` and `calculateSum`) much easier, because both require you to **return** values rather than simply print them.









I'm glad this pace is working well. We'll continue exactly in the order of your Baeldung resource.

---

# 📚 Lesson 2 – Part 3: Method Identifier

Baeldung says:

> **The method identifier is the name we assign to a method specification.**

Let's break that down.

---

# What is a Method Identifier?

A **method identifier** is simply the **name of the method**.

For example:

```java
public static void printMessage() {

}
```

The method identifier is:

```text
printMessage
```

It's the name Java uses to identify this method.

Think of it like a person's name.

If you say:

> "Mike"

everyone knows who you're referring to.

Similarly, when Java sees:

```java
printMessage();
```

it knows exactly which method to execute.

---

# Where is the Method Identifier?

Let's look at another example.

```java
public static String greetUser(String name) {
    return "Hello " + name;
}
```

Break it down:

```text
public      → access modifier
static      → keyword
String      → return type
greetUser   → method identifier
(String name) → parameter list
```

The method identifier always comes **after the return type**.

---

# Why Do We Need a Method Name?

Imagine a class with several methods.

```java
public class Main {

    static void greetUser() {

    }

    static void calculateSum() {

    }

    static void printReport() {

    }

}
```

Each method performs a different task.

Without names, Java wouldn't know which one you wanted to call.

When you write:

```java
calculateSum();
```

Java looks for the method whose identifier is `calculateSum`.

---

# Choosing Good Method Names

Baeldung says:

> **It is good practice to use an informative and descriptive name.**

This means the name should clearly describe what the method does.

Good examples:

```java
calculateSum()
```

```java
printReport()
```

```java
greetUser()
```

From just the name, you can already guess the method's purpose.

---

# Poor Method Names

These names don't explain the method well:

```java
method1()
```

```java
doThing()
```

```java
abc()
```

If someone else reads your code, they won't know what those methods are supposed to do.

This is why Baeldung recommends descriptive names.

---

# Java Naming Convention

Baeldung also says:

> **The method identifier should be a verb in lowercase that can be followed by adjectives and/or nouns.**

Let's look at what that means.

### Start with a verb

A verb describes an action.

Examples:

```text
print
calculate
save
read
write
get
set
```

---

### Add more words if needed

```text
printMessage
```

Verb:

```text
print
```

Noun:

```text
Message
```

---

Another example:

```text
calculateSum
```

Verb:

```text
calculate
```

Noun:

```text
Sum
```

---

Another:

```text
greetUser
```

Verb:

```text
greet
```

Noun:

```text
User
```

This naming style makes code much easier to read.

---

# Java Uses camelCase

Notice something about these names.

```text
calculateSum
```

The first word starts with a lowercase letter.

Each following word starts with a capital letter.

This style is called **camelCase**.

Examples:

```text
printName
```

```text
getAge
```

```text
calculateTotalPrice
```

Baeldung doesn't explicitly explain camelCase, but all of its examples follow this Java naming convention.

---

# Interesting Fact from Baeldung

The article mentions:

> **A method identifier can have at most 65,536 characters.**

Technically, Java allows extremely long method names.

For example (don't do this in practice!):

```java
calculateTheTotalPriceIncludingTaxAndShippingForAllProducts()
```

This is valid, but unnecessarily long.

The important takeaway is simply that Java has a maximum limit, even though you'll never come close to it in normal programming.

---

# Summary

From Baeldung:

* The **method identifier** is the method's name.
* It comes after the return type.
* Java uses it to identify and call the method.
* Choose informative and descriptive names.
* Method names should usually begin with a verb.
* Java uses camelCase for method names.
* A method identifier can be up to **65,536 characters** long.

---

# 📝 Quick Check

### Question 1

What is the method identifier?

```java
public static int calculateSum(int a, int b) {

}
```

---

### Question 2

According to Baeldung, what kind of names should methods have?

---

### Question 3

Which of these is the better method name?

```text
method1()
```

or

```text
calculateAverage()
```

Why?

---

### Question 4

Where does the method identifier appear?

A.

Before the return type

B.

After the return type

C.

Inside the parameter list

---

### Question 5

Identify every part we've learned so far:

```java
public static String greetUser(String name) {
    return "Hello " + name;
}
```

Try to identify:

* Access modifier
* `static`
* Return type
* Method identifier

*(Don't worry about the parameter list yet—that's our next topic.)*

---

# 📌 Progress Check

So far, you've learned **4 of the 6 parts** that Baeldung describes:

| Part                                      | Status     |
| ----------------------------------------- | ---------- |
| ✅ Access modifier                         | Complete   |
| ✅ `static` keyword (explained in context) | Complete   |
| ✅ Return type                             | Complete   |
| ✅ Method identifier                       | Complete   |
| ⏳ Parameter list                          | Next       |
| ⏳ Exception list                          | After that |
| ⏳ Method body                             | Final part |

Notice that we're slowly building the ability to "read" a method from left to right. By the end of Lesson 2, you'll be able to look at almost any basic Java method and explain what every part means, which is exactly what your course resources are aiming for.
