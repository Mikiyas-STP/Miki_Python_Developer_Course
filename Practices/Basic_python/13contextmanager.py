from contextlib import contextmanager

@contextmanager
def admin_session(user_name: str):
    print(f"AUDIT: User {user_name} started a session.")
    try:
        yield
    finally:
        print(f"AUDIT: User {user_name} closed the session.")
        # The 'finally' block runs NO MATTER WHAT
        # even if the code inside the 'with' crashed.


with admin_session("Alice") as session:
    print(" Alice is deleting old logs...")
    print("   Alice is updating user permissions...")

    # Output should be:
# AUDIT: User Alice started a session.
#    Alice is deleting old logs...
#    Alice is updating user permissions...
# AUDIT: User Alice closed the session.





# 🧠 Deep Question: The as Keyword
# In your code, you wrote with admin_session("Alice") as session:.
# Currently, the variable session will be equal to None.
# Question: If I wanted the session variable to contain a unique ID (like a random string), where would I put that ID in my admin_session function?

@contextmanager
def admin_session(user_name: str, session_id: int):
    print(f"START: User {user_name} (ID: {session_id})")
    
    # Whatever we yield here becomes the 'session' variable!
    yield f"SESSION_TOKEN_{session_id}" 
    
    print(f"END: User {user_name}")

with admin_session("Alice", 123) as session:
    print(f"Using {session}") # Prints: Using SESSION_TOKEN_123