def yuza(r):
    a = 3
    s = p * r ** 2
    return s
# Learn Global Local Types in python


def peremetr(s):

    global p
    p = 3.14
    return 2 * p * s


print(yuza(21))
print(peremetr(peremetr))
