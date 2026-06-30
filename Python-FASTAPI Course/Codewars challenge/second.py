users = [
    {"id": 1, "name": "Alice", "age": 20},
    {"id": 2, "name": "Bob", "age": 30},
    {"id": 3, "name": "Charlie", "age": 25}
]


def get_usernames(records: list) -> list:
    names = []
    for user in records:
        names.append(user["name"])
    return names

def get_users_over_21(records: list) -> list:
    result = []
    for user in records:
        if user["age"] > 21:
            result.append(user)
    return result

users.append( {"id": 4, "name": "sody", "age": 21})


def update_user_age(records: list, name: str, new_age: int) -> list:
    for user in records:
        if user["name"] == name:
            user["age"] = new_age
    return records


#clean solution option B
users = [
    {"id": 1, "name": "Alice", "age": 20},
    {"id": 2, "name": "Bob", "age": 30},
    {"id": 3, "name": "Charlie", "age": 25}
]


def get_usernames(records: list) -> list:
    return [user["name"] for user in records]


def get_users_over_21(records: list) -> list:
    return [user for user in records if user["age"] > 21]


def add_user(records: list, user: dict) -> list:
    records.append(user)
    return records


def update_user_age(records: list, name: str, new_age: int) -> list:
    for user in records:
        if user["name"] == name:
            user["age"] = new_age
    return records


# Usage
print(get_usernames(users))
print(get_users_over_21(users))

add_user(users, {"id": 4, "name": "sody", "age": 21})
update_user_age(users, "Bob", 35)

print(users)

# What you just wrote is basically:

# GET users
# FILTER users
# CREATE user
# UPDATE user
# 👉 That’s CRUD (core backend concept)

def delete_user_by_id(records: list, user_id: int) -> list:
    return [ users for users in records if users["id"] != user_id ]

#alternative approach
def delete_user_by_id(records: list, user_id: int) -> None:
    for i, user in enumerate(records):
        if user["id"] == user_id:
            records.pop(i)
            break
#for both the deleted and undeleted items
def delete_user_by_id(records: list, user_id: int):
    updated_list = []
    deleted_user = None

    for user in records:
        if user["id"] == user_id:
            deleted_user = user
        else:
            updated_list.append(user)

    return updated_list, deleted_user

