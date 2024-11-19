# Reverse Integer

num = int(input("Enter a number: "))
is_negative = num < 0
numStr = str(abs(num))
numList = list(numStr)
numList.reverse()
numStr = "".join(numList)

reversed_num = int(numStr)
if is_negative:
    reversed_num = -reversed_num

print(reversed_num)
