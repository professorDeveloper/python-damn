# Tub Son
number = int(input("N: "))  # 3
for i in range(1, number + 1):
    count = 0  #
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(f"{i} -> tub son")
    else:
        print(i)
