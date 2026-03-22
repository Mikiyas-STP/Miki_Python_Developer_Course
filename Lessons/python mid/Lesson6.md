### Topic 6: Iterators and Generators

In backend engineering, we often deal with **Large Data**. Imagine you have a database with 10,000,000 logs. 

If you do `logs = get_all_logs()`, your server will try to load all 10 million rows into the RAM (Memory) at once. **The server will crash.**

**Generators** solve this. Instead of giving you the whole list at once, a generator gives you **one item at a time**, only when you ask for it.

#### 1. The `yield` Keyword
In a normal function, we use `return`. In a generator, we use `yield`. 
`yield` is like a "Pause" button. It gives you a value, then waits until you ask for the next one.

```python
def simple_generator():
    print("--- Starting ---")
    yield 1
    yield 2
    yield 3

gen = simple_generator()

print(next(gen)) # Prints 1
print(next(gen)) # Prints 2
```

#### 2. Real-World Backend Example: Reading a Giant File
Instead of loading a 5GB file into memory, we read it line by line.

```python
def read_huge_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

# This uses almost ZERO memory, even if the file is huge!
for line in read_huge_file("server_logs.txt"):
    if "ERROR" in line:
        print(line)
```

---

### Your Coding Challenge: The "Batch Processor"

Imagine you have a list of 1,000,000 user IDs. You need to send them to an email service, but the service only allows you to send **100 IDs at a time**.

**Task:**
1.  Create a generator function called `get_batches`.
2.  It should take two arguments: a `data_list` and a `batch_size`.
3.  Inside, use a `for` loop and **Slicing** (remember `list[start:stop]`?) to grab a chunk of the data.
4.  Use `yield` to return that chunk.

**Starter Code:**
```python
def get_batches(data_list, batch_size):
    # TODO: Loop through the data_list in steps of batch_size
    # TODO: yield a slice of the list
    pass

# Test data (numbers 1 to 10)
numbers = list(range(1, 11)) 

# We want batches of 3
for batch in get_batches(numbers, 3):
    print(f"Sending batch to API: {batch}")

# Expected Output:
# Sending batch: [1, 2, 3]
# Sending batch: [4, 5, 6]
# Sending batch: [7, 8, 9]
# Sending batch: [10]
```

**Senior Hint:** To loop in steps, you can use `range(0, len(data_list), batch_size)`.

**Show me your first Generator!11batchprocessor.py** This is a key skill for handling heavy data in Python.

**Answer in 12batchprocessor.py** 