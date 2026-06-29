# 📚 Lesson 3 – Method Signatures

**Based entirely on:**

* Baeldung – *Methods in Java*
* Your learning objectives

---

# 🎯 Learning Objectives

By the end of this lesson, you should be able to:

* Explain what a method signature is.
* Identify the components of a method signature.
* Explain which parts are **not** part of a method signature.
* Read a method signature.
* Understand the workshop question:

  > **What are the components of a method signature? Are any of them optional?**

---

# What Baeldung Says

Baeldung gives the definition:

> **A method signature is comprised of only two components — the method's name and parameter list.**

This sentence is one of the most important in this topic.

Notice the word:

> **only**

That means everything else we've learned **is not part of the method signature**.

---

# What Is a Method Signature?

A **method signature** is **not** the entire method.

Instead, it is just a way of identifying a method using:

1. **Method name**
2. **Parameter list**

Nothing else.

---

# Think Back to Lesson 2

We learned that a method declaration can contain:

```text
Access modifier
Return type
Method identifier
Parameter list
Exception list
Method body
```

Now Baeldung tells us:

A **method signature** is much smaller.

It contains only:

```text
Method identifier
+
Parameter list
```

---

# Example 1

Consider this method:

```java
public static String greetUser(String name) {
    return "Hello " + name;
}
```

Let's identify everything.

| Part              | Value           |
| ----------------- | --------------- |
| Access modifier   | `public`        |
| `static`          | `static`        |
| Return type       | `String`        |
| Method identifier | `greetUser`     |
| Parameter list    | `(String name)` |
| Method body       | `{ ... }`       |

Now the question is:

**What is the method signature?**

Answer:

```text
greetUser(String name)
```

Notice what disappeared.

There is **no**:

* `public`
* `static`
* `String`
* method body

Only:

* method name
* parameter list

---

# Example 2

```java
private int calculateSum(int a, int b) {

    return a + b;

}
```

The signature is:

```text
calculateSum(int a, int b)
```

Again:

Everything else is ignored.

---

# Example 3

```java
void printMessage() {

}
```

Signature:

```text
printMessage()
```

Even an empty parameter list is still part of the signature.

---

# What Is NOT Part of the Signature?

Baeldung's definition lets us answer this directly.

The following are **not** part of a method signature:

❌ Access modifier

```java
public
```

❌ `static`

```java
static
```

❌ Return type

```java
String
```

❌ `throws`

```java
throws IOException
```

❌ Method body

```java
{

}
```

Only these remain:

✅ Method name

✅ Parameter list

---

# Reading a Signature

Suppose someone writes:

```text
calculateSum(int first, int second)
```

Without seeing the full method, you already know:

Method name:

```text
calculateSum
```

Parameters:

```text
int first

int second
```

You do **not** know:

* whether it's `public`
* whether it's `private`
* whether it's `static`
* what it returns

Because those things are **not part of the signature**.

---

# Parameter Names vs Parameter Types

Look carefully at this method:

```java
public int add(int a, int b) {

}
```

Signature:

```text
add(int a, int b)
```

Now another method:

```java
public int add(int first, int second) {

}
```

Signature:

```text
add(int first, int second)
```

Notice something.

The **parameter names changed**.

The **parameter types stayed the same**.

Baeldung includes the full parameter list in the signature, including the names, because it's describing the declaration as written. However, from Java's perspective when distinguishing overloaded methods, it's the **method name and parameter types** that matter, not the parameter names. Your course doesn't go into that compiler detail here, so for this lesson, follow Baeldung's simpler definition:

> A method signature consists of the method name and the parameter list.

---

# Why Is This Important?

Your workshop asks:

> **What are the components of a method signature?**

You can now answer:

> A method signature consists of **the method name (method identifier)** and **the parameter list**.

---

# Are Any Components Optional?

Another workshop question asks:

> **Are any of them optional?**

Let's think.

A method signature has:

1. Method name
2. Parameter list

Can a method exist without a name?

No.

Can a method exist without parentheses?

No.

Even if there are no parameters:

```java
printMessage()
```

the parameter list still exists.

It is simply empty.

Therefore:

**Neither component is optional.**

The parameter list may be **empty**, but it is still present.

---

# Summary

According to Baeldung:

A method signature contains only:

* Method identifier
* Parameter list

It does **not** include:

* Access modifier
* `static`
* Return type
* Exception list
* Method body

Both parts of the signature are required.

---

# 📝 Knowledge Check

## Question 1

What is the method signature?

```java
public static void greet() {

}
```

---

## Question 2

What is the method signature?

```java
private String getName(String firstName, String lastName) {

}
```

---

## Question 3

Which of these are part of a method signature?

* Access modifier
* Return type
* Method identifier
* Parameter list
* Method body

---

## Question 4

True or False?

The return type is part of the method signature.

---

## Question 5

Answer the workshop question in your own words:

> **What are the components of a method signature? Are any of them optional?**

---

## 📌 End of Lesson 3

This lesson completes the core concept of **method signatures**, one of the main learning objectives in your course.
