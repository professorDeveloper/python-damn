# task1
def maxNumWithoutValue(a: int, b: int, c: int):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)


def tortburchaPerimetrniHisoblash(a: int, b: int) -> int:
    return 2 * a + b


def yuzaTortBurchak(a: int, b: int) -> int:
    return a * b


def checkJuftToq(a: int) -> bool:
    return a % 2 == 0


def find_max(a: int, b: int, c: int) -> int:
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def factorial(n: int) -> int:
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def fibonacci(n: int) -> []:
    fibonacciNum = [0, 1]
    for i in range(2, n):
        fibonacciNum.append(fibonacciNum[i - 1] + fibonacciNum[i - 2])
    return fibonacciNum


print(fibonacci(10))


# Task Do Fibonacci in  using Recursive
# F(n) = F(n-1) + F(n-2) va F(0) = 0, F(1) = 1
def fibonacciWithRecursive(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    print(fibonacciWithRecursive(number-1)+fibonacciWithRecursive(number-2))
    return fibonacciWithRecursive(number - 1) + fibonacciWithRecursive(number - 2)


result = fibonacciWithRecursive(10)
print(result)

