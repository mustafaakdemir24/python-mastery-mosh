print(type(5))
print(type(range(5)))

# Iterable
for x in list([1, 2, 3, 4]):
    print(x)

print("------------------")

# While Loop #
number = 100
while number > 0:
    print(number)
    number //= 2

print("------------------")

################
while True:
    command = input(">")
    print(f"ECHO {command}")
    if command.lower() == "quit":
        break
