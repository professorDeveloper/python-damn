# Reverse String II

def reverse(string, k):
    if k != 0 and k < len(string):
        lastArr = []
        firstArr = []
        lastReverse = string[len(string) - k:]
        middle = string[k + 1:len(string) - k]
        firstReverse = string[0:k]
        for i in lastReverse:
            lastArr.append(i)
        for i in firstReverse:
            firstArr.append(i)
        firstArr.reverse()
        lastArr.reverse()
        lastReverse = ""
        firstReverse = ""
        for i in lastArr:
            lastReverse += i
        for i in firstArr:
            firstReverse += i
        return firstReverse + middle + lastReverse


print(reverse("Hello World", 2))
