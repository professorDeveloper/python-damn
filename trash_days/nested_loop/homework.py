# Task1
matrix = [[1, 2, 3], {4, 5, 6}, [7, 8, 9]]
count = 0
for i in matrix:
    for j in i:
        if j % 2 == 0:
            count += 1

print(f"Juft Sonlar Soni :{count}")

# Task2
matrix = [[1, 2, 3], {4, 5, 6}, {7, 8, 9}]

for itemList in matrix:
    for j in itemList:
        # Find tub
        tubCount = 0
        for i in range(1, j + 1):
            if j % i == 0:
                tubCount += 1
        if tubCount == 2:
            print("Siz tubson kiritdingiz")
        else:
            print(j)


#    int number = 12345;
#     int count = 0;
#     while (true) {
#     int result = number % 10;
#     number = number / 10;
#     if (result == 5) {
#     count++;
#     break;
#     }
#     }
#

# While Day
count =0
numer =125
while numer != 0 :
    if numer % 10 == 0:
        count+=1

print(count)