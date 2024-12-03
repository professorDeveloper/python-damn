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
    fibonacciNum = [1, 1]
    for i in range(2, n):
        fibonacciNum.append(fibonacciNum[i - 1] + fibonacciNum[i - 2])
    return fibonacciNum


print(fibonacci(10))

# Task Do Fibonacci in  using Recursive
