# plus func positioned
def plus(a, b, /) -> int:
    return a + b


# minus func named
def minus(*, a, b) -> int:
    return a - b


# multiply func positioned
def multiply(a, b, ) -> int:
    return a * b


print(multiply(2, 2))


def divide( a, /,*,b, ) -> int:
    return a // b


print(divide(3, b=3))
