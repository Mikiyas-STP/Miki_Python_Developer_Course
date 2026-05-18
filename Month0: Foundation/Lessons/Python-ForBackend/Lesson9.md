# Topic 9: Virtual Environments and Dependency Management

In backend development, you don't just write your own code. You use **Packages** (libraries) written by other people. For example:
*   **FastAPI**: To build the API.
*   **SQLAlchemy**: To talk to the database.
*   **Requests**: To talk to other websites.

### The Problem: "But it works on my machine!"
Imagine you build a project using **FastAPI version 1.0**. Six months later, you start a new project using **FastAPI version 2.0**. If you install both on your computer, they might fight each other, and your old project will break.

### The Solution: Virtual Environments (`venv`)
A virtual environment is a **private folder** for your project. Everything inside that folder (the Python version and the packages) stays there. It doesn't touch the rest of your computer.

#### How to use it (The basic commands):
1.  **Create it:** `python -m venv venv` (This creates a folder named `venv`).
2.  **Activate it:** 
    *   Windows: `venv\Scripts\activate`
    *   Mac/Linux: `source venv/bin/activate`
3.  **Install things:** `pip install requests` (This installs the "Requests" library).

---

### Managing Dependencies: `requirements.txt`

When you share your backend code with a team, you don't send them the `venv` folder (it's too big). Instead, you send a tiny text file called `requirements.txt`.

This file lists every package your project needs.
*   **To create it:** `pip freeze > requirements.txt`
*   **To install from it:** `pip install -r requirements.txt`

---

### Your Coding Challenge: The "Package Explorer"

We are going to simulate managing a project. Since we are in a chat, you can't run the `venv` commands, but I want you to show me you understand the logic.

**Task:**
1.  Imagine you are starting a new project called "PaymentGateway".
2.  What is the **first command** you should run in your terminal to create a virtual environment?
3.  If you want to install a package called `stripe`, what command do you type?
4.  Write a small Python script that uses the `logging` module to log an **INFO** message saying: `"Environment Setup Complete. Ready to use package: stripe"`

---

### 🧠 Senior Question:
Why should we **never** upload the `venv` folder to GitHub? (Think about the size of the folder and the different operating systems of your teammates).


### Senior Code Review

**The `venv` Name**
* `python3 -m venv venv`
* `source venv/bin/activate` 
* `logging.info("...")`. Also, remember we must call `logging.basicConfig(level=logging.INFO)` first, or the message won't show up!


### 🧠 Answering the Senior Question
**Why do we never upload `venv` to GitHub?**

1.  **Size:** A `venv` can be 100MB to 500MB. GitHub is for code (KB), not massive library folders.
2.  **Portability:** A `venv` created on **Windows** will not work on **Mac** or **Linux**. 
3.  **The Solution:** We only upload `requirements.txt`. When your teammate downloads the code, they run `pip install -r requirements.txt` to build their *own* fresh environment for their specific computer.