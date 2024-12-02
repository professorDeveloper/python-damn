m = 5
n = 5
parking = []
for i in range(m):
    row = []
    for j in range(n):
        row.append("0")
    parking.append(row)

for i in range(m):
    for j in range(n):
        print(parking[i][j], end=" ")
    print()
while True:
    row = int(input("Qator raqami: "))
    col = int(input("Ustun raqami: "))
    carName = input("Mashina nomi: ")
    parking[row][col] = carName
    print(f"{row} qator {col} ustunga {carName} mashina qoyildi")
    for i in range(m):
        for j in range(n):
            print(parking[i][j], end=" ")
        print()

