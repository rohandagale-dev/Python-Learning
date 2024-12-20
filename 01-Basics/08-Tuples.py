# Empty tuple
empty_tuple = ()

# Tuple with elements
my_tuple = (1, 2, 3)

# Tuple without parentheses (tuple packing)
my_tuple = 1, 2, 3

# Single-element tuple (comma is required)
single_tuple = (1,)  # Correct
not_a_tuple = (1)    # This is an integer, not a tuple

my_tuple = (10, 20, 30, 40)

# Access by index
print(my_tuple[0])  # Output: 10

# Negative indexing
print(my_tuple[-1])  # Output: 40

# Slicing
print(my_tuple[1:3])  # Output: (20, 30)

tuple1 = (1, 2)
tuple2 = (3, 4)

# Concatenation
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4)

# Repetition
result = tuple1 * 3
print(result)  # Output: (1, 2, 1, 2, 1, 2)

my_tuple = (1, 2, 3)
print(2 in my_tuple)   # Output: True
print(5 not in my_tuple)  # Output: True

my_tuple = (1, 2, 3)
for item in my_tuple:
    print(item)

my_tuple = (1, 2, 3, 2, 4, 2)
print(my_tuple.count(2))  # Output: 3

my_tuple = (1, 2, 3, 2, 4)
print(my_tuple.index(2))  # Output: 1

# Attempt to modify (will raise an error)
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

my_tuple = (1, 2, 3)

# Convert to list
temp_list = list(my_tuple)
temp_list[0] = 10

# Convert back to tuple
my_tuple = tuple(temp_list)
print(type(my_tuple))  # Output: (10, 2, 3)

# Packing
packed_tuple = 1, 2, 3

# Unpacking
a, b, c = packed_tuple
print(a, b, c)  # Output: 1 2 3

# Unpacking with *
my_tuple = (1, 2, 3, 4, 5)
a, *b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4]
print(c)  # Output: 5

nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple[1])      # Output: (2, 3)
print(nested_tuple[1][0])   # Output: 2
