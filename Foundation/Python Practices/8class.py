class User:
    # Class Variable (Shared by all users)
    VERSION = 1.0

    def __init__(self, username: str, email: str, role: str = "guest"):
        self.username = username
        self.email = email
        self.role = role

    def get_profile(self) -> str:
        return f"User {self.username} is a {self.role}."

    def is_admin(self) -> bool:
        return self.role == "admin"

if __name__ == "__main__":
    # 1. Create instances (The "Houses")
    admin_user = User("mike", "mike@test.com", "admin")
    guest_user = User("sara", "sara@test.com") # Role defaults to "guest"

    # 2. Call methods on the instances
    print(admin_user.get_profile()) # Python passes admin_user as 'self'
    print(f"Is Admin? {admin_user.is_admin()}")

    print(guest_user.get_profile())
    print(f"Is Admin? {guest_user.is_admin()}")
    
    # 3. Accessing a Class Variable
    print(f"System Version: {User.VERSION}")