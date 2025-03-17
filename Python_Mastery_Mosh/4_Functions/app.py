def greet(name):
    print(f"Hi {name}")

# print(greet("Mosh"))

# Keyword Arguments


def increment(number, by):
    return number + by

# print(increment(2, by=1))

# Default Arguments


def increment1(number, by=1):
    return number + by

# print(increment1(2, 5))

# xargs


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

# print(multiply(2, 3, 4, 5))

# xxargs


def save_user(**user):
    print(user["name"])

# save_user(id=1, name="John", age=22)

# Scope


message = "a"


def greet1(name):
    global message
    message = "b"

# greet1("Mosh")
# print(message)

# Debugging


def multiply1(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiply1(1, 2, 3))
