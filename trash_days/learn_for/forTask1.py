row = int(input("Row: "))
column = int(input("Column: "))
for i in range(0, row):
    for j in range(column):
        if i % 2 == 0:
            if j % 2 == 0:
                print(0, end=" ")
            else:
                print(1, end=' ')
        else:
            if j % 2 == 0:
                print(1, end=" ")
            else:
                print(0, end=' ')
    print()
