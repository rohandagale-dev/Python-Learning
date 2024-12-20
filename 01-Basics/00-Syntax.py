# Basic printing
print("hello world")


# Variables and Data types
x = 10  # int
pi = 3.14  # Float
name = "Alice"  # String
is_Valid = True  # Boolean


# Input and Output
take_input = input("Enter your name: ")
print(take_input)


# Conditional statement
age = int(input("Enter your age: "))

if age < 18:
    print("You're minor")
elif age == 18:
    print("Welcome to adulhood")
else:
    print("You are an adult")


# Loops
count = 0
while (count < 5):
    print(count)
    count += 1


# Functions
def greet(name):
    print("hello "+name)
greet("rohan")


# Lists (Arrays)
hero = ["Ironman", "Spiderman", "Hulk"]
print(hero)


# Tuples
coordinates = (10, 20, 20)
print(coordinates)