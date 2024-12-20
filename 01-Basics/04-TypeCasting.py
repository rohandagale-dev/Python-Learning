# Implicit conversion from int to float
num_int = 10
num_float = 2.5

result = num_int + num_float
print(result)         # Output: 12.5
print(type(result))   # Output: <class 'float'>

# Convert float to int
num_float = 5.6
num_int = int(num_float)
print(num_int)        # Output: 5

# Convert int to string
num = 123
num_str = str(num)
print(num_str)        # Output: '123'
print(type(num_str))  # Output: <class 'str'>

# Convert string to float
s = "3.14"
num = float(s)
print(num)            # Output: 3.14

# Convert list to tuple
lst = [1, 2, 3]
tpl = tuple(lst)
print(tpl)            # Output: (1, 2, 3)

# Convert tuple to list
tpl = (4, 5, 6)
lst = list(tpl)
print(lst)            # Output: [4, 5, 6]
