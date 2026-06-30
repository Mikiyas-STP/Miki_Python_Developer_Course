### Lesson 6: Arrays — The Foundation of Data Structures

In JavaScript, an Array is a magical, flexible object that can grow, shrink, and hold strings, numbers, and objects all at once. **In Java, Arrays are "Low-Level" and strict.**

#### 1. What problem does this solve?
If you need to store 100 integers, you don't want to create 100 variables (`int1`, `int2`...). You need a way to store a sequence of data in a single contiguous block of memory.

#### 2. Why does it exist?
Arrays are the most basic way to group data. They are designed for **maximum performance**. Because an array has a fixed size, the computer knows exactly where every element is located in memory, making access (e.g., `myArray[50]`) lightning fast.

#### 3. How does it work internally?
When you create `int[] arr = new int[5];`, Java allocates a **fixed block of memory** on the Heap.
*   If an `int` is 4 bytes, this array takes exactly 20 bytes.
*   **Crucial Point:** You **cannot** change the size of a Java array after it is created. If you need more space, you have to create a *new* bigger array and copy the old values over.

#### 4. Example in Java
```java
// Declaration and Initialization
int[] scores = new int[3]; 
scores[0] = 90;
scores[1] = 85;
scores[2] = 100;

// Shorthand
String[] names = {"Alice", "Bob", "Charlie"};

System.out.println(names.length); // 3
```

#### 5. Comparison with JavaScript and Python
*   **JS/Python:** `list = [1, "two", 3.0]`. Arrays are dynamic and "heterogeneous" (mixed types).
*   **Java:** `int[] arr = {1, 2, 3}`. Arrays are **fixed-size** and "homogeneous" (all elements must be the same type). 

*Note: In Java, if you want a JS-like array, you use an `ArrayList`, which we will cover in the next sprint. But under the hood, `ArrayList` is just a class that manages a standard Java Array!*

#### 6. Real-world industry usage
We rarely use raw Arrays in high-level business logic (we prefer `List`). However, we use them in:
*   **Performance-critical code:** Image processing, crypto, or high-frequency trading.
*   **IO Buffers:** Reading chunks of data from a file or network.
*   **The `main(String[] args)` method:** Passing command-line arguments.

#### 7. Common mistakes
*   **`ArrayIndexOutOfBoundsException`:** Trying to access index `3` in an array of size `3` (indices are 0, 1, 2). This is the #1 Java beginner error.
*   **Printing an Array:** If you do `System.out.println(myArray)`, Java prints the **memory address** (e.g., `[I@15db9742`), not the contents. You have to use a loop or `Arrays.toString(myArray)`.

#### 8. Mini Exercise: The Search
Write a simple method that takes an `int[]` and an `int target`. It should return the **index** of the target if found, or `-1` if not found.

```java
public int findIndex(int[] numbers, int target) {
    // Your code here
}
```

#### 9. Interview perspective
**Question:** "What is the time complexity of accessing an element in an array by its index?"
**The 'Senior' Answer:** "It is **O(1)** or Constant Time. Because the array is stored in a contiguous block of memory and the size of each element is known, the JVM calculates the exact memory address using the formula: `baseAddress + (index * elementSize)`. It doesn't need to iterate through the array to find the value."

#### 10. Key takeaways
*   Arrays have a **fixed size**.
*   Arrays are **objects** (stored on the Heap).
*   Indices start at **0**.
*   They provide the fastest possible access to a collection of data.

---
