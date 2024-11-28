# task5
# num to two system num
num = int(input("num:"))
# input =4
# output =100
qoldiq=[]
qoldiqStr=""
while num>0:
    data =num%2
    qoldiq.append(data)
    num =num//2
qoldiq.reverse()

for i in qoldiq:
    qoldiqStr+=str(i)
print(int(qoldiqStr))