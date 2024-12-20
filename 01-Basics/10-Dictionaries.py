# Empty dictionary
my_dict = {}

# Dictionary with elements
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Using keyword arguments
my_dict = dict(name="Alice", age=25, city="New York")
print(my_dict)

# From a list of tuples
my_dict = dict([("name", "Alice"), ("age", 25), ("city", "New York")])

my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])  # Output: Alice

print(my_dict.get("age"))  # Output: 25
print(my_dict.get("city", "Not Found"))  # Output: Not Found

# Add a new key-value pair
my_dict["age"] = 25

# Update an existing key's value
my_dict["name"] = "Bob"

print(my_dict)  # Output: {'name': 'Bob', 'age': 25}

# Removing elements
my_dict = {"name": "Alice", "age": 25}
age = my_dict.pop("age")  # raises a keyError if not found
print(age)  # Output: 25
print(my_dict)  # Output: {'name': 'Alice'}

# Delete both key and value
my_dict = {"name": "Alice", "age": 25}
del my_dict["age"]  # Removes the key 'age'
# del my_dict  # Deletes the entire dictionary
print(my_dict)  # Output: {'name': 'Alice'}

# Iteration
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Checking membership
my_dict = {"name": "Alice", "age": 25}
print("name" in my_dict)  # Output: True
print("city" not in my_dict)  # Output: True

# Nested dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

print(nested_dict["person1"]["name"])  # Output: Alice

# Combining dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

result = dict1 | dict2
print(result)  # Output: {'a': 1, 'b': 3, 'c': 4}
