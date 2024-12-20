import sys

# Integer
x = 10
print("Size of integer:", sys.getsizeof(x), "bytes")

# Float
pi = 3.14
print("Size of float:", sys.getsizeof(pi), "bytes")

# String
name = "Alice"  # 1 byte per character
print("Size of string is: 41 +", sys.getsizeof(name) - 41, "bytes")

# List
numbers = [1, 2, 3, 4, 5]  # 8 byte per element
print("Size of list: 56 +", sys.getsizeof(numbers) - 56, "bytes")

# Dictionary
data = {"name": "Alice", "age": 25}
print("Size of dictionary: 64 +", sys.getsizeof(data) - 64, "bytes")

# Tuple
tup = (1, 2, 3, 4, 5)  # 8 byte per element
print("Size of dictionary: 40 +", sys.getsizeof(tup) - 40, "bytes")
