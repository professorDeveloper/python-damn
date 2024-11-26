mlist = [2, 3, 4, 1, 45, 12, 33]
for i in range(0, len(mlist)):
    for j in range(0, len(mlist) - i - 1):
        if mlist[j] > mlist[j + 1]:
            mlist[j], mlist[j + 1] = mlist[j + 1], mlist[j]

print(f"Sorted List:{mlist}")

# Bubble sort example