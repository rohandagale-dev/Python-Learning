# Empty list
my_list = []

# List with elements
my_list = [1, 2, 3, "Python", [4, 5]]

# Using the list() constructor
my_list1 = list(my_list)  # Converts a tuple to a list

print(my_list1)

# Indexing
print(my_list1[0])
print(my_list1[-1])

# Slicing
print(my_list1[1:4])  # last element is ignored
print(my_list1[:3])
print(my_list1[::2])

# Append element
my_list1.append(10)
my_list1.extend([12, 14])
print(my_list1)

# Remove element
my_list1.remove([4, 5])
print(my_list1.pop())
print(my_list1)

# Count frequency of element
print(my_list1.count(3))

# Reverse list
my_list1.reverse()

print(my_list1)
