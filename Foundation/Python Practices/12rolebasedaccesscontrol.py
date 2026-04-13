import asyncio
import logging

# THE MODEL
class User:
    def __init__(self, username: str, is_active: bool = True ):
        self.username = username
        self.is_active = is_active
        # TODO: Initialize self.tags as a SET containing the string "admin"
        self.tags = {"Admin"}

# THE SECURITY GUARD (DECORATOR)
def require_admin(func):
    async def wrapper(user_obj, *args, **kwargs):
        # TODO: Update this condition. 
        # Access is granted ONLY IF user is active AND "admin" is in their tags.
        if user_obj.is_active and "Admin" in user_obj.tags : # <--- Fix this line
            return await func(user_obj, *args, **kwargs)
        else:
            return f"Access Denied for {user_obj.username}"
    return wrapper

# THE SERVICE
class AdminService:
    @require_admin
    async def delete_user(self, user_obj: User, target_name: str):
        await asyncio.sleep(0.5)
        return f"SUCCESS: {user_obj.username} deleted {target_name}"

# THE EXECUTION
async def main():
    # Test 1: An active Admin
    boss = User("chief_dev", is_active=True)
    service = AdminService()
    
    result = await service.delete_user(boss, "guest_user_01")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())