# The `await` Secret (Advanced Knowledge)**
# Your Answer:"We use await to tell our system we need to wait."
# The Senior Detail:** You are correct, but here is the "Mid-level" secret: `await` doesn't just wait; it **yields control**. It tells the Python **Event Loop**: *"I'm going to be busy for a second. You are free to go run other code while I wait for this database."* 
# What if you forget `await`?** Python won't wait. It will return a "Coroutine Object" (basically a promise that hasn't started yet) and move to the next line immediately. Your code will likely crash because it tries to use data that doesn't exist yet!


import asyncio

async def check_db(user: str):
    await asyncio.sleep(1)
    return "User Verified"

async def send_email(user: str):
    await asyncio.sleep(1)
    return "Email Sent"

async def login(user: str):
    print(f"--- Login started for {user} ---")
    
    # We pass 'user' to the functions and capture the list of results
    results = await asyncio.gather(check_db(user), send_email(user))
    
    # results will be ['User Verified', 'Email Sent']
    print(f"Status: {results}")

if __name__ == "__main__":
    # Total time: 1 second (because they ran at the same time!)
    asyncio.run(login("David"))