#Task 4
list =[1,2,1,2,4]
for i in range(0,len(list)):
    if list.count(list[i]) ==1:
        print(list[i])
        break
