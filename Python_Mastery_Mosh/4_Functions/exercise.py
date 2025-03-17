def fizz_buzz(input):
    if input % 3 == 0:
        if input % 5 == 0:
            return "FizzBuzz"
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(7))
