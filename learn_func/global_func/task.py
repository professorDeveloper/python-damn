# Task1
def min(a, b, c, d, e):
    if a < b and a < c and a < d and a < e:
        return a
    elif b < c and b < d and b < e and b < a:
        return b
    elif c < b and c < d and c < d and c < e and c < a:
        return c
    elif c > d and d < b and d < e and a > d:
        return d
    elif e < b and e < d and e < a and c > e:
        return e


print(max(1, 2, 3, 4, 5))


# Task2
def checkNatural(a: float):
    if a < 0:
        print("Natural Son")
    else:
        print("Natural son emas")

def checkStr(word:str):
    maxCount = 0
    minCount = 0
    for i in word:
        if i.islower():
            minCount += 1
        elif i.isupper():
            maxCount += 1
    print(f"{word} so`zida {minCount} ta kichik harf {maxCount} ta katta harf    ")
