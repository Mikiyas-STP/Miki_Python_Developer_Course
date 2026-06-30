def build_query(table: str, **filters) -> str:
    conditions = ", ".join([f"{k}='{v}'" for k, v in filters.items()])
    return f"SELECT * FROM {table} WHERE {conditions}"


def generate_search_summary(search_term: str, **kwargs) -> str:
    if not kwargs:
        return f"Searching for '{search_term}' with no filters"
    
    filters_str = ", ".join([f"{key}={value}" for key, value in kwargs.items()])
    return f"Searching for '{search_term}' with filters: {filters_str}"






def create_api_user(username: str, role: str, email: str):
    print(f"Creating {role}: {username} ({email})")

# Data from an API/Database
user_data = {
    "username": "sara_dev",
    "role": "admin",
    "email": "sara@company.com"
}

# Instead of: create_api_user(user_data["username"], user_data["role"]...)
# We do this:
create_api_user(**user_data) 