### Lesson 5: Control Flow — Writing "Professional" Logic

In your PERN stack experience, you’ve written thousands of `if/else` statements. In Java, the syntax is almost identical to JavaScript, but the **philosophy** of how we structure logic in enterprise systems is different.

#### 1. What problem does this solve?
Code is a series of decisions. However, "Spaghetti Code" (deeply nested `if` statements) is the #1 cause of bugs in production. If you have an `if` inside an `if` inside an `if`, it becomes impossible to test all the paths.

#### 2. Why does it exist?
Control flow (`if`, `else`, `switch`, `for`, `while`) allows the program to be dynamic. In Java, because of **Static Typing**, the compiler ensures that the condition inside an `if` statement **must** evaluate to a `boolean`. 

*In JS, you can do `if (1) { ... }` (truthy). In Java, `if (1)` will fail to compile. It must be `if (x == 1)`.*

#### 3. How does it work internally?
At the Bytecode level, these are "Jump" instructions. The CPU evaluates a condition and then "jumps" to a different memory address to continue execution.

#### 4. Example: The "Guard Clause" Pattern
Professional Java developers avoid the "Arrow Shape" (deep nesting). 

**Junior Style (The Nested Mess):**
```java
public void processOrder(Order order) {
    if (order != null) {
        if (order.isPaid()) {
            if (order.hasStock()) {
                // Ship the order
            } else {
                System.out.println("No stock");
            }
        } else {
            System.out.println("Not paid");
        }
    }
}
```

**Senior Style (The Guard Clause):**
```java
public void processOrder(Order order) {
    if (order == null) return; // Guard clause
    if (!order.isPaid()) {
        System.out.println("Not paid");
        return;
    }
    if (!order.hasStock()) {
        System.out.println("No stock");
        return;
    }

    // Ship the order - "The Happy Path" is now at the top level
}
```

#### 5. Comparison with JavaScript and Python
*   **JavaScript:** Uses `===` to avoid type coercion. In Java, we only have `==` for primitives, and it is always strict.
*   **Python:** Uses indentation for blocks. Java uses curly braces `{}`. **Senior Tip:** Even if your `if` statement is only one line, *always* use curly braces. It prevents bugs during future refactoring.

#### 6. Real-world industry usage: The `switch` statement
In modern Java (Java 17+), the `switch` statement has become very powerful. We use it to handle multiple states (like Order Status: PENDING, SHIPPED, DELIVERED).

```java
String message = switch (status) {
    case "PENDING" -> "Order is being prepared";
    case "SHIPPED" -> "Order is on the way";
    default -> "Unknown status";
};
```

#### 7. Common mistakes
*   **The "Else-If" Chain of Doom:** If you have more than 3 `else if` statements, you should probably be using a `switch` or a Design Pattern (like the *Strategy Pattern*).
*   **Comparing Strings with `==`:** I will repeat this forever—never use `if (name == "Admin")`. Always use `if ("Admin".equals(name))`.

#### 8. Mini Exercise: The "Happy Path"
Refactor this "Junior" code into "Senior" code using **Guard Clauses**.

```java
public String getDiscount(int age, boolean isMember) {
    String result = "No Discount";
    if (isMember) {
        if (age > 65) {
            result = "Senior Member Discount";
        } else {
            result = "Standard Member Discount";
        }
    }
    return result;
}
```

#### 9. Interview perspective
**Question:** "What is the difference between `while` and `do-while` loops?"
**The 'Senior' Answer:** "A `while` loop checks the condition **before** executing the block; if the condition is false, it may never run. A `do-while` loop executes the block **at least once** before checking the condition. In production, `while` is much more common, as `do-while` can often lead to unexpected side effects if not handled carefully."

#### 10. Key takeaways
*   **Fail Fast:** Use Guard Clauses to exit a method as early as possible.
*   **Keep the "Happy Path" clean:** The main logic of your method should not be buried inside 4 sets of curly braces.
*   **Strict Booleans:** Java doesn't have "truthy" or "falsy" values like JS.

---

**How would you refactor that discount logic?** Once you show me, we will tackle the final part of the Prep: **Arrays and the introduction to the Collections Framework.**


Answer
```java
public String getDiscount(int age, boolean isMember) {
    // 1. Guard Clause: Handle the "unhappy" or "simple" path first
    if (!isMember) {
        return "No Discount";
    }

    // 2. If we are here, we KNOW they are a member. 
    // We don't need an 'else' because the 'return' above acts as a wall.
    if (age > 65) {
        return "Senior Member Discount";
    }

    // 3. The final "Happy Path"
    return "Standard Member Discount";
}
```
