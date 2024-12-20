# Types of error
# RuntimeError, TypeError, NameError
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        raise ValueError("Invalid input")


x = int(input("Input a number"))
print(x)
