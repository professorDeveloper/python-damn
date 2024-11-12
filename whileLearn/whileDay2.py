count = 0
numer = 125
while numer > 0:
    numer =numer // 10
    count += 1


print(count)


# Task1
i =1
sum=0
while i <= 100:
    sum = sum + i
    i = i + 1
print(sum)

# Task2
juftSum =0
toqSum =0
i =0
while i <= 50:
    if i%2==0:
        juftSum =juftSum +i
    else :
        toqSum =toqSum +i
    i = i + 1
print(juftSum)
print(toqSum)
# Task3
i=-80
count =0
while i<80:
    if i%7==0:
        count=count+1
    i = i + 1
print(count)