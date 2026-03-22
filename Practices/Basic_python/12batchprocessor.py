def get_batches(data_list: list, batch_size: int):
    # i will be 0, then 3, then 6, then 9
    for i in range(0, len(data_list), batch_size):
        # We start at 'i' and go for 'batch_size' steps
        yield data_list[i : i + batch_size]

# --- Let's trace it ---
# Round 1: i=0 -> yield data_list[0:3]  -> [1, 2, 3]
# Round 2: i=3 -> yield data_list[3:6]  -> [4, 5, 6]
# Round 3: i=6 -> yield data_list[6:9]  -> [7, 8, 9]
# Round 4: i=9 -> yield data_list[9:12] -> [10]
# --- Test ---
numbers = list(range(1, 11)) 
for batch in get_batches(numbers, 3):
    print(f"Batch: {batch}")

# 🧠 Answering the "Memory" Question
# (You missed this one, but it's the most important part of the lesson for a backend engineer!)
# Question: Why is a Generator better than a List for 1,000,000 rows?
# The Senior Answer:
# A List requires RAM for every single item at the same time. If 1,000,000 rows take 2GB of memory and your server only has 1GB free, the server will crash with an OutOfMemory error.
# A Generator only keeps one batch in memory at a time. It processes 100 items, throws them away, then grabs the next 100. This allows you to process a 50GB database on a tiny, cheap server. This is called "Streaming" data.
