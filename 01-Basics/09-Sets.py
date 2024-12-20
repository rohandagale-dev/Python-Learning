# Empty set
my_set = set()  # Correct way to create an empty set
not_a_set = {}  # This creates a dictionary, not a set

# Set with elements
my_set = {1, 2, 3}

# From a string (splits into unique characters)
my_set = set("hello")  # Output: {'h', 'e', 'l', 'o'}

# From a list
my_set = set([1, 2, 3, 3, 4])  # Output: {1, 2, 3, 4}
print(my_set)

my_set = {1, 2, 3}

for item in my_set:
    print(item)

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# Upate add multipe elements
my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements
my_set = {1, 2, 3}
my_set.remove(2)  # raises keyError if element not found
print(my_set)  # Output: {1, 3}

# Discard
my_set = {1, 2, 3}
my_set.discard(4)  # No error
print(my_set)  # Output: {1, 2, 3}

# Pop
my_set = {1, 2, 3}
removed_item = my_set.pop()  # raises keyError if set is empty
print(removed_item)  # Output: An arbitrary element (e.g., 1)
print(my_set)        # Output: Remaining elements

# Clear
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()

# Set Membership
my_set = {1, 2, 3}

# Check if an element exists in the set
print(2 in my_set)  # Output: True
print(5 not in my_set)  # Output: True

# Mathematical set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)  # OR: set1 | set2
print(result)  # Output: {1, 2, 3, 4, 5}

# Difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.difference(set2)  # OR: set1 - set2
print(result)  # Output: {1, 2}

# Symmetric Difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.symmetric_difference(set2)  # OR: set1 ^ set2
print(result)  # Output: {1, 2, 4, 5}

# Frozen set
frozen = frozenset([1, 2, 3])
print(frozen)  # Output: frozenset({1, 2, 3})

# Immutable: Raises AttributeError
# frozen.add(4)

# Convertion
# List to set
my_set = set([1, 2, 3, 3])
print(my_set)  # Output: {1, 2, 3}

# Set to list
my_list = list(my_set)
print(my_list)  # Output: [1, 2, 3]
