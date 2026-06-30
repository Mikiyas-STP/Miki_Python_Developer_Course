Excellent. You've now finished the core topics from your worksheet. The next session is one that beginners often skip over, but it's very important because you'll use it constantly when working with arrays, lists, and collections.

---

# 📚 Session 7 — Enhanced `for` Loop (For-each Loop)

## Learning Objectives

By the end of this session, you will be able to:

* Explain what an enhanced `for` loop is.
* Understand how it differs from a standard `for` loop.
* Know when to use each.
* Iterate through arrays and collections.
* Explain why the enhanced `for` loop exists.

---

# 1. Why Was the Enhanced `for` Loop Introduced?

Suppose we have an array:

```java
int[] numbers = {10, 20, 30, 40, 50};
```

If we want to print every number, we can use a normal `for` loop:

```java
for (int i = 0; i < numbers.length; i++) {
    System.out.println(numbers[i]);
}
```

This works perfectly.

But notice something...

We never actually use `i` for anything except getting the next element.

The enhanced `for` loop removes this unnecessary work.

---

# 2. The Syntax

```java
for (Type variable : collection) {

    // use variable

}
```

This looks strange at first.

Read it like English:

> **For each element in this collection, put it into this variable and execute the code.**

---

# Example

```java
int[] numbers = {10, 20, 30, 40, 50};

for (int number : numbers) {
    System.out.println(number);
}
```

Output

```text
10
20
30
40
50
```

Notice that there is:

* no index (`i`)
* no `.length`
* no `i++`

Java does all of that for you.

---

# 3. Breaking Down the Syntax

```java
for (int number : numbers)
```

Let's analyse every part.

### `int`

The type of each element.

Our array contains integers:

```java
int[] numbers
```

so each element is an `int`.

---

### `number`

This is a temporary variable.

On each iteration Java copies one element into it.

Iteration 1

```text
number = 10
```

Iteration 2

```text
number = 20
```

Iteration 3

```text
number = 30
```

...

---

### `:`

Many beginners ask:

> "What does `:` mean?"

Think of it as:

> **"in"** or **"from"**

So

```java
for (int number : numbers)
```

can be read as:

> **For each number in numbers...**

---

### `numbers`

The array (or collection) we are looping through.

---

# 4. What Java Does Behind the Scenes

When you write

```java
for (int number : numbers)
```

Java is effectively doing something like this behind the scenes:

```java
for (int i = 0; i < numbers.length; i++) {

    int number = numbers[i];

    System.out.println(number);

}
```

The enhanced `for` loop is simply a shorter, cleaner way of writing a common pattern.

---

# 5. Visualising the Loop

Array:

```text
Index

0   1   2   3   4

10 20 30 40 50
```

Iteration 1

```text
number = 10
```

Iteration 2

```text
number = 20
```

Iteration 3

```text
number = 30
```

Iteration 4

```text
number = 40
```

Iteration 5

```text
number = 50
```

Loop ends.

---

# 6. Standard `for` vs Enhanced `for`

Standard:

```java
for (int i = 0; i < numbers.length; i++) {

    System.out.println(numbers[i]);

}
```

Enhanced:

```java
for (int number : numbers) {

    System.out.println(number);

}
```

Both produce exactly the same output.

The difference is readability.

---

# 7. When Should You Use the Enhanced `for` Loop?

Use it when:

* You want to read every element.
* You don't need the index.
* You won't change the collection while looping.

Example:

```java
String[] names = {
    "Mike",
    "Sarah",
    "James"
};

for (String name : names) {
    System.out.println(name);
}
```

Output

```text
Mike
Sarah
James
```

---

# 8. When Should You NOT Use It?

Suppose you want:

```text
1. Mike
2. Sarah
3. James
```

You need the position.

Enhanced `for` doesn't tell you which position you're on.

Instead, use:

```java
for (int i = 0; i < names.length; i++) {

    System.out.println((i + 1) + ". " + names[i]);

}
```

---

Another example.

Suppose you want only every second element.

```text
10
30
50
```

You need the index.

Standard `for` is better.

---

# 9. Arrays vs Collections

Enhanced `for` works on both.

Array

```java
int[] numbers = {1,2,3};
```

Collection (you'll learn this later)

```java
List<String> names = List.of("Mike","Sarah","John");
```

Both work:

```java
for (String name : names)
```

---

# 10. Common Beginner Mistakes

## Mistake 1

Trying to access an index.

```java
for (int number : numbers) {

    System.out.println(numbers[number]);

}
```

Wrong.

`number` is already the value.

If `number` is `20`, Java will try to access:

```java
numbers[20]
```

which is probably outside the array.

---

Correct:

```java
System.out.println(number);
```

---

## Mistake 2

Using the enhanced `for` when you need the index.

Example:

```text
1. Apple
2. Orange
3. Banana
```

Impossible with only:

```java
for (String fruit : fruits)
```

because you don't know the current position.

---

# 11. Comparison Table

| Feature                        | Standard `for` | Enhanced `for` |
| ------------------------------ | -------------- | -------------- |
| Has index                      | ✅ Yes          | ❌ No           |
| Simpler syntax                 | ❌ No           | ✅ Yes          |
| Works with arrays              | ✅ Yes          | ✅ Yes          |
| Works with collections         | ✅ Yes          | ✅ Yes          |
| Skip elements                  | ✅ Yes          | ❌ Difficult    |
| Reverse order                  | ✅ Yes          | ❌ No           |
| Best for reading every element | Good           | Excellent      |

---

# Real-world Examples

### Print all students

```java
for (String student : students) {
    System.out.println(student);
}
```

---

### Print every product

```java
for (Product product : products) {
    System.out.println(product);
}
```

---

### Print every order

```java
for (Order order : orders) {
    System.out.println(order);
}
```

This is exactly how Java backend developers work with data from databases and APIs.

---

# Summary

The enhanced `for` loop:

* Iterates through every element in an array or collection.
* Is shorter and easier to read than a standard `for` loop.
* Does **not** give you the index.
* Is ideal when you only need the values.

Think of it as:

> **"For each element in this collection, do something with it."**

---

# Mini Quiz

Answer these without looking back.

### 1. What problem does the enhanced `for` loop solve?

---

### 2. Read this aloud in English:

```java
for (String name : names)
```

---

### 3. What does the `:` symbol mean in an enhanced `for` loop?

---

### 4. When would you choose a standard `for` loop instead?

---

### 5. What will this print?

```java
String[] fruits = {"Apple", "Orange", "Banana"};

for (String fruit : fruits) {
    System.out.println(fruit);
}
```

---

### 6. Which loop would you use if you need to print:

```text
1. Apple
2. Orange
3. Banana
```

Why?

---

## 💡 Think Like an Engineer

Imagine you're building a Java backend that receives a list of 1,000 customer orders from a database.

Your task is to calculate the total price of all orders.

**Question:** Would you use a standard `for` loop or an enhanced `for` loop? Explain your choice.

---

## 🎯 Where You Are Now

You've completed all the topics from your worksheet:

* ✅ Session 1 – Java Basics
* ✅ Session 2 – Variables & Primitive Types
* ✅ Session 3 – Java Keywords
* ✅ Session 4 – `if` / `else`
* ✅ Session 5 – `for` Loops
* ✅ Session 6 – `switch`
* ✅ Session 7 – Enhanced `for` Loops

The natural next step isn't just another language feature—it's learning **how to combine these concepts to solve problems**. That's where you'll start thinking like a software engineer rather than just learning Java syntax.

