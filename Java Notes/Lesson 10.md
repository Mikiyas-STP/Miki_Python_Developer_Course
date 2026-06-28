This is where programming starts to become **logical** rather than just syntactical.

As a software engineer, most of your code is simply answering one question:

> **"Should I do this or not?"**

That's exactly what conditional statements solve.

---

# 📚 Session 4 — Conditional Statements (`if`, `else if`, `else`)

## Learning Objectives

By the end of this session, you will:

* Understand what a condition is.
* Use comparison operators.
* Use logical operators.
* Write `if`, `if-else`, and `if-else if` statements.
* Understand nested `if` statements.
* Know when to use `if` instead of `switch`.

---

# 1. What is a Condition?

A **condition** is an expression that evaluates to either:

```java
true
```

or

```java
false
```

Remember from Session 2:

```java
boolean
```

stores only:

* `true`
* `false`

Conditions always produce one of these two values.

---

## Example

```java
int age = 20;

age >= 18
```

Ask yourself:

> Is 20 greater than or equal to 18?

Yes.

Result:

```java
true
```

---

Another example:

```java
age < 18
```

Is 20 less than 18?

No.

Result:

```java
false
```

---

# 2. Comparison Operators

These compare two values.

| Operator | Meaning               | Example      |
| -------- | --------------------- | ------------ |
| `==`     | Equal to              | `age == 18`  |
| `!=`     | Not equal to          | `age != 18`  |
| `>`      | Greater than          | `score > 50` |
| `<`      | Less than             | `price < 10` |
| `>=`     | Greater than or equal | `age >= 18`  |
| `<=`     | Less than or equal    | `age <= 65`  |

---

### Example

```java
int marks = 75;

System.out.println(marks > 50);
```

Output:

```
true
```

---

# ⚠️ Common Beginner Mistake

Many beginners write:

```java
if (age = 18)
```

❌ Wrong.

Why?

Because:

```java
=
```

means **assignment**.

You're trying to assign a value, not compare it.

Correct:

```java
if (age == 18)
```

`==` means **comparison**.

---

# 3. The `if` Statement

An `if` statement runs code **only if** the condition is true.

```java
int age = 20;

if (age >= 18) {
    System.out.println("Adult");
}
```

Let's follow the program:

```
age = 20

↓

20 >= 18 ?

↓

true

↓

Print "Adult"
```

---

Now:

```java
int age = 15;

if (age >= 18) {
    System.out.println("Adult");
}
```

```
15 >= 18 ?

↓

false

↓

Skip the block
```

Nothing is printed.

---

# 4. `if-else`

Sometimes you want two possible outcomes.

```java
int age = 15;

if (age >= 18) {
    System.out.println("Adult");
} else {
    System.out.println("Minor");
}
```

If the first condition is false, Java executes the `else` block.

---

# Flow

```
Condition

↓

true?

↓

YES → if block

NO

↓

else block
```

---

# 5. `else if`

Suppose you want more than two choices.

Example:

```java
int score = 82;

if (score >= 90) {
    System.out.println("Grade A");
}
else if (score >= 80) {
    System.out.println("Grade B");
}
else if (score >= 70) {
    System.out.println("Grade C");
}
else {
    System.out.println("Fail");
}
```

Java checks **from top to bottom**.

The **first true condition wins**.

---

### Why order matters

Imagine:

```java
score = 95;
```

If you write:

```java
if (score >= 70)
```

first,

Java prints:

```
Grade C
```

and stops.

It never reaches:

```java
score >= 90
```

That's why you should check the **most specific** or **highest** conditions first.

---

# 6. Nested `if`

An `if` inside another `if`.

Example:

```java
int age = 20;
boolean hasTicket = true;

if (age >= 18) {

    if (hasTicket) {
        System.out.println("You may enter.");
    }

}
```

Think of it like two security checks:

```
Are you over 18?

↓

Yes

↓

Do you have a ticket?

↓

Yes

↓

Enter
```

---

# 7. Logical Operators

Sometimes one condition isn't enough.

---

## AND (`&&`)

Both conditions must be true.

```java
if (age >= 18 && hasTicket) {
    System.out.println("Welcome");
}
```

| Age ≥ 18 | Ticket | Result |
| -------- | ------ | ------ |
| ✅        | ✅      | ✅      |
| ✅        | ❌      | ❌      |
| ❌        | ✅      | ❌      |
| ❌        | ❌      | ❌      |

---

## OR (`||`)

Only one condition must be true.

```java
if (isAdmin || isTeacher) {
    System.out.println("Access granted");
}
```

| Admin | Teacher | Result |
| ----- | ------- | ------ |
| ✅     | ❌       | ✅      |
| ❌     | ✅       | ✅      |
| ✅     | ✅       | ✅      |
| ❌     | ❌       | ❌      |

---

## NOT (`!`)

Reverses a boolean.

```java
boolean isLoggedIn = false;

if (!isLoggedIn) {
    System.out.println("Please log in.");
}
```

`!false` becomes `true`, so the message is printed.

---

# Real-world Example

Suppose you're writing login logic.

```java
String username = "Mike";
String password = "Java123";
boolean accountLocked = false;
```

You might check:

```java
if (!accountLocked) {
    System.out.println("Login allowed.");
}
```

This is clearer than writing:

```java
if (accountLocked == false)
```

---

# Common Mistakes

## Assignment instead of comparison

❌

```java
if (age = 18)
```

✅

```java
if (age == 18)
```

---

## Comparing Strings with `==`

This is a preview of a future topic.

```java
String name = "Mike";

if (name == "Mike")
```

Although this may sometimes appear to work, the correct way to compare `String` values is with `.equals()`:

```java
if (name.equals("Mike"))
```

We'll explore why later when we discuss objects and memory.

---

## Forgetting braces

```java
if (age >= 18)
    System.out.println("Adult");
    System.out.println("Welcome");
```

Only the first `println` belongs to the `if`.

To avoid bugs, always use braces:

```java
if (age >= 18) {
    System.out.println("Adult");
    System.out.println("Welcome");
}
```

---

# Exercise

Write a program that:

1. Creates:

```java
int age = 20;
```

2. Prints:

```
Adult
```

if age is 18 or above.

Otherwise print:

```
Minor
```

---

## Challenge 1

Create:

```java
int score = 85;
```

Print:

* A
* B
* C
* Fail

using an `if-else if` ladder.

---

## Challenge 2

Create:

```java
boolean hasTicket = true;
int age = 22;
```

Print:

```
Entry allowed
```

only if:

* age is at least 18
* **and** the person has a ticket.

---

# Summary

You now know:

* ✅ What a condition is.
* ✅ Comparison operators.
* ✅ Logical operators (`&&`, `||`, `!`).
* ✅ `if`, `else`, and `else if`.
* ✅ Nested `if` statements.
* ✅ Common beginner mistakes.

---

# Mini Quiz

Answer without looking back.

### 1. What is a condition?

---

### 2. What is the difference between:

```java
=
```

and

```java
==
```

---

### 3. What does `&&` mean?

---

### 4. What does `||` mean?

---

### 5. What does `!` do?

---

### 6. What will this print?

```java
int age = 16;

if (age >= 18) {
    System.out.println("Adult");
}
else {
    System.out.println("Minor");
}
```

---

### 7. What will this print?

```java
int score = 95;

if (score >= 70) {
    System.out.println("C");
}
else if (score >= 90) {
    System.out.println("A");
}
```

**Explain why.**

---

## Think Like an Engineer

Before you answer the quiz, here's a question to develop your reasoning:

Suppose you're checking whether a user can access an online exam.

They must:

* be logged in,
* have paid for the course,
* and the exam must be open.

**Question:** Would you use `&&` or `||` to combine these conditions? More importantly, **why?** This is the kind of reasoning you'll use constantly in backend development.


1) a condition is a statement to check for a specific argument 
2) = is assignments where as == is checking for value 
3) && means and 
4) OR 
5) not 
6) minor 
7) C because it will  check the first and pass it. 

Excellent. You got **6 out of 7** correct, and more importantly, your explanations are improving. Let's review them like a senior engineer would.

---

# 1. What is a condition?

> **Your answer:**
>
> "a condition is a statement to check for a specific argument"

### ✅ Almost correct (8.5/10)

The word **argument** isn't the right term here.

A better definition is:

> **A condition is an expression that evaluates to either `true` or `false`. It is used to decide which code should be executed.**

For example:

```java
age >= 18
```

This expression evaluates to either:

* `true`
* `false`

---

# 2. Difference between `=` and `==`

> **Your answer:**
>
> "`=` is assignments whereas `==` is checking for value"

### ✅ 10/10

Perfect.

Remember:

```java
age = 18;
```

means:

> Put the value `18` into `age`.

Whereas:

```java
age == 18
```

means:

> Is `age` equal to `18`?

---

# 3. What does `&&` mean?

> **Your answer:**
>
> "and"

### ✅ 10/10

Exactly.

It means **both conditions must be true**.

Example:

```java
if (age >= 18 && hasTicket)
```

Both conditions must be satisfied.

---

# 4. What does `||` mean?

> **Your answer:**
>
> "OR"

### ✅ 10/10

Correct.

Only one condition needs to be true.

---

# 5. What does `!` do?

> **Your answer:**
>
> "not"

### ✅ 10/10

Correct.

It reverses a boolean value.

```java
true
```

becomes

```java
false
```

and vice versa.

---

# 6. What will this print?

```java
int age = 16;

if (age >= 18) {
    System.out.println("Adult");
}
else {
    System.out.println("Minor");
}
```

> **Your answer:**
>
> "Minor"

### ✅ 10/10

Exactly.

Because:

```java
16 >= 18
```

is

```java
false
```

So Java executes the `else` block.

---

# 7. What will this print?

```java
int score = 95;

if (score >= 70) {
    System.out.println("C");
}
else if (score >= 90) {
    System.out.println("A");
}
```

> **Your answer:**
>
> "C because it will check the first and pass it."

### ✅ 10/10

Excellent!

This is a very common interview question.

The important idea is:

Java checks conditions **from top to bottom**.

Let's trace it:

```text
score = 95

↓

95 >= 70 ?

↓

true

↓

Print "C"

↓

Stop
```

Java never even reaches:

```java
score >= 90
```

That's why the order of conditions matters.

A better version would be:

```java
if (score >= 90) {
    System.out.println("A");
}
else if (score >= 70) {
    System.out.println("C");
}
```

Now `95` correctly prints `A`.

---

# Engineer's Question

Earlier, I asked:

> A user can access an exam only if they:
>
> * are logged in,
> * have paid,
> * and the exam is open.

Would you use:

```java
&&
```

or

```java
||
```

**Why?**

Think carefully before answering. This type of logic appears constantly in backend development, APIs, and authentication systems.

---

# Overall Progress

You've now covered:

* ✅ Session 1 – Java Basics
* ✅ Session 2 – Variables & Primitive Types
* ✅ Session 3 – Java Keywords
* ✅ Session 4 – Conditional Statements

Your understanding is becoming more **reasoning-based**, which is exactly what you want. Instead of memorising syntax, you're starting to explain **why** Java behaves the way it does. That's the mindset of a software engineer.
 

