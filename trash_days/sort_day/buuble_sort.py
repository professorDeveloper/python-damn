# Learn buble sort

my_list = [2, 3, 4, 1, 6, 12, 33, 0, 1]
# after 1,4

for i in range(0, len(my_list)):
    for j in range(0, len(my_list) - 1):
        if my_list[j] > my_list[j + 1]:  # 2>3 =false,3>4=false,4>1=true
            temp = my_list[j]
            my_list[j] = my_list[j + 1]
            my_list[j + 1] = temp

print(my_list)

# Buuble sort 2-type

for i in range(len(my_list)):
    for j in range(0, len(my_list)):
        if my_list[i] < my_list[j]:
            temp = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = temp
print(my_list)
