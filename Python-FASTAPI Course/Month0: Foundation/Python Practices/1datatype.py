# Excercise 1
# The raw data we received from the API
api_response = {
    "username": "  charlie_dev  ",
    "access_level": 5,
    "tags":["python", "backend"]
}

# 1. Access with brackets (or .get)
# 2. Chain .strip() to cut the whitespace
clean_username = api_response["username"].strip()

#TODO2:Safely get the "is_active" status from the dict.
#The API forgot to send it! Use .get() to default it to False.

# .get("string_key", default_value)
is_active = api_response.get("is_active", False)

#TODO3:Append the string "api_v2" to the "tags" list inside the dictionary.
api_response["tags"].append("api_v2")

#TODO4:Create an f-string that says: "User charlie_dev has access level 5."
#Use the clean_username variable you created, and the access_level from the dict.
log_message = f"User {clean_username} has access level {api_response['access_level']}."


# Print out your results to test them!
print(clean_username)
print(is_active)
print(api_response["tags"])
print(log_message)




#Excercise 2
server_config = {
    "host": "localhost",
    "port": 8080,
    "allowed_methods": ["GET", "POST"]
}

# TODO 1: Extract the "host" from the dictionary using bracket notation.
host_name = server_config["host"]

# TODO 2: The dictionary is missing a "timeout" key. 
# Use .get() to safely extract "timeout" and give it a default value of 30.
timeout_limit = server_config.get("timeout",30)

# TODO 3: Append the string "PUT" to the "allowed_methods" list inside the dictionary.
server_config["allowed_methods"].append("PUT")


# Print to check your work
print(host_name)
print(timeout_limit)
print(server_config["allowed_methods"])