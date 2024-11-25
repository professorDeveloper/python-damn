# Learn buble sort
my_list = [2, 3, 4, 1, 6, 12, 33, 0]
for i in range(0, len(my_list)):
    for j in range(0, len(my_list) - 1):
        if my_list[j] > my_list[j + 1]:
            temp = my_list[j]
            my_list[j] = my_list[j + 1]
            my_list[j + 1] = temp

print(my_list)
