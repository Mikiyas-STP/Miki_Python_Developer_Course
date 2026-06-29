# 📚 Lesson 2 – Part 4: Parameter List

## 🎯 Learning Objectives

By the end of this section, you should be able to:

* Explain what a parameter list is.
* Identify parameters in a method.
* Understand that a method can have 0 to 255 parameters.
* Recognise different types of parameters.

---

# What Baeldung Says

Baeldung states:

> **We can specify input values for a method in its parameter list, which is enclosed in parentheses.**

Let's break this into smaller pieces.

---

# What is a Parameter List?

A **parameter list** defines the **inputs** that a method expects.

Think of a method as a small machine.

```
Input  ─────►  Method  ─────►  Output
```

Some machines need inputs to work.

For example, imagine a calculator.

If you ask it to add two numbers, you first have to provide those numbers.

Similarly, a Java method often needs information before it can do its job.

That information is provided through **parameters**.

---

# Where is the Parameter List?

Look at this method:

```java
public static String greetUser(String name) {
    return "Hello, " + name;
}
```

Let's identify the parts we've learned.

```text
public          → Access modifier
static          → Keyword
String          → Return type
greetUser       → Method identifier
(String name)   → Parameter list
```

Everything inside the parentheses is the **parameter list**.

---

# A Method Can Have No Parameters

Some methods don't need any input.

Example:

```java
public static void sayHello() {
    System.out.println("Hello!");
}
```

Notice the parentheses:

```java
()
```

They're empty.

This means the method doesn't require any information from whoever calls it.

---

# A Method Can Have One Parameter

Example:

```java
public static void greetUser(String name) {
    System.out.println("Hello, " + name);
}
```

Parameter list:

```java
(String name)
```

This method expects one piece of information:

* Type: `String`
* Name: `name`

---

# A Method Can Have Multiple Parameters

Example:

```java
public static int calculateSum(int a, int b) {
    return a + b;
}
```

Parameter list:

```java
(int a, int b)
```

There are two parameters.

| Type  | Name |
| ----- | ---- |
| `int` | `a`  |
| `int` | `b`  |

Notice that the parameters are separated by a comma.

---

# Every Parameter Has Two Parts

Every parameter consists of:

1. A **type**
2. A **name**

Example:

```java
String name
```

Break it down:

```text
String  → type
name    → parameter name
```

Another example:

```java
int age
```

Break it down:

```text
int  → type
age  → parameter name
```

---

# Different Types of Parameters

Baeldung says:

> **A parameter can be an object, a primitive or an enumeration.**

Based on what you've learned so far, let's focus on the examples you've already seen.

Primitive parameter:

```java
int age
```

Object parameter:

```java
String name
```

The article also mentions **enumerations**, but since it doesn't explain them here, you only need to know that Java allows them as parameter types. We'll study enums when your course introduces them.

---

# How Many Parameters Can a Method Have?

Baeldung mentions an interesting fact:

> **A method can have anywhere from 0 to 255 parameters.**

Examples:

No parameters:

```java
printMessage()
```

One parameter:

```java
printMessage(String message)
```

Two parameters:

```java
calculateSum(int a, int b)
```

Technically, Java allows up to **255** parameters.

In practice, however, most methods use only a few.

---

# Parentheses Always Exist

Notice something important.

Even when there are no parameters, the parentheses are still required.

Correct:

```java
sayHello()
```

Incorrect:

```java
sayHello
```

The parentheses tell Java that you're dealing with a method.

---

# Summary

From Baeldung:

* The **parameter list** provides the inputs a method needs.
* It is written inside parentheses `()`.
* A method can have:

  * 0 parameters
  * 1 parameter
  * many parameters (up to 255)
* Each parameter has:

  * a type
  * a name
* Parameters are separated by commas.

---

# 📝 Knowledge Check

Try these without looking back.

### Question 1

What is the parameter list?

---

### Question 2

How many parameters does this method have?

```java
public static void printMessage() {

}
```

---

### Question 3

Identify the parameters.

```java
public static int add(int first, int second) {

}
```

---

### Question 4

Every parameter consists of which two parts?

---

### Question 5

According to Baeldung, what is the maximum number of parameters a method can have?

---

## 📌 Progress Tracker

You've now completed **5 of the 6 parts** of a Java method:

| Part                | Status     |
| ------------------- | ---------- |
| ✅ Access modifier   | Complete   |
| ✅ Return type       | Complete   |
| ✅ Method identifier | Complete   |
| ✅ Parameter list    | Complete   |
| ⏳ Exception list    | Next       |
| ⏳ Method body       | After that |

After the next two sections, you'll have covered **all six components** exactly as presented in your Baeldung resource. Then we'll move on to **Method Signatures**, which is the next major topic in your course.
