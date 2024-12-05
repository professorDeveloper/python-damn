def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


a = factorial(5)
print(a)


def sum(a):
    if a > 1:
        return a + sum(a - 1)
    else:
        return 1


def numbersSum(a):
    if a > 0:
        return a % 10 + numbersSum(a // 10)
    else:
        return 0


print(numbersSum(24))


def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(10))


