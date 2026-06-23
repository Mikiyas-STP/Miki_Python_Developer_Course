### Compiled Languages

A **compiler** translates the entire program into machine code **before execution**.

**Flow:**

```text
Source Code → Compiler → Executable Machine Code → Run
```

**Examples:**

* C
* C++
* Go
* Rust

**Advantages:**

* Faster execution
* Errors caught before running
* Better performance for large systems

---

### Interpreted Languages

An **interpreter** translates and executes the code **line by line at runtime**.

**Flow:**

```text
Source Code → Interpreter → Execute
```

**Examples:**

* Python
* JavaScript
* Ruby

**Advantages:**

* Faster development and testing
* More flexible
* Easier debugging

---

### Real-World Note

The distinction is not always strict.

For example:

* Java is compiled into **bytecode** and then run on the **JVM**.
* Python is first compiled into **bytecode** (`.pyc`) and then interpreted by the Python Virtual Machine.

### Interview Answer (1 sentence)

> A compiled language translates the whole program into machine code before execution, whereas an interpreted language translates and executes code at runtime, usually line by line.







**Is Java Fully Compiled**

No, **Java is not fully compiled to native machine code in the traditional sense**.

Java uses a **hybrid approach** that combines compilation and interpretation.

### How Java Works

```text
Java Source Code (.java)
        ↓
      javac
        ↓
Bytecode (.class)
        ↓
JVM (Java Virtual Machine)
        ↓
Machine Code
```

#### Step 1: Compilation

The Java compiler (`javac`) converts `.java` files into **bytecode** (`.class` files).

Bytecode is **not machine code**. It is an intermediate format designed to run on any JVM.

#### Step 2: JVM Execution

The JVM executes the bytecode.

Initially, the JVM may interpret the bytecode, but modern JVMs use a **Just-In-Time (JIT) compiler**, which converts frequently used bytecode into native machine code while the program is running.

---

## What Makes Java Different?

### 1. "Write Once, Run Anywhere"

With C:

```text
C Source → Compiler → Windows Executable
```

To run on Linux, you must recompile.

With Java:

```text
Java Source → Bytecode
```

The same bytecode can run on:

* Windows
* Linux
* macOS

As long as a JVM exists for that platform.

This portability is Java's most famous feature.

---

### 2. JVM Provides an Abstraction Layer

The JVM sits between your code and the operating system.

```text
Your Code
    ↓
   JVM
    ↓
Operating System
```

Benefits:

* Platform independence
* Automatic memory management (Garbage Collection)
* Security features
* Runtime optimisations

---

### 3. JIT Compilation

Unlike traditional compiled languages:

* C compiles once before execution.
* Java compiles twice:

  * `.java` → bytecode
  * bytecode → machine code (during execution)

The JVM can observe how your application behaves and optimise hot code paths.

This is why Java often performs much better than people expect.

---

### Comparison

| Language   | Compilation Model                                  |
| ---------- | -------------------------------------------------- |
| C          | Fully compiled to machine code before running      |
| C++        | Fully compiled to machine code before running      |
| Python     | Mostly interpreted by the Python runtime           |
| JavaScript | Interpreted/JIT compiled by the browser or runtime |
| Java       | Compiled to bytecode, then JIT compiled by the JVM |

### Engineering Summary

A good interview answer would be:

> Java is neither purely compiled nor purely interpreted. It is compiled into platform-independent bytecode, which is then executed and optimised by the JVM using interpretation and Just-In-Time compilation. This gives Java portability, strong runtime optimisation, and good performance across different operating systems.
