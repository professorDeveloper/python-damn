# Learn bubble sort

my_list = [2, 3, 4, 1, 6, 12, 33, 0, 1]
# after 1,4
count = 0
for i in range(0, len(my_list)):
    for j in range(0, len(my_list) - 1):
        count = count + 1
        if my_list[j] > my_list[j + 1]:  # 2>3 =false,3>4=false,4>1=true
            temp = my_list[j]
            my_list[j] = my_list[j + 1]
            my_list[j + 1] = temp

print(my_list)
print(count)
# Bubble sort 2-type
my_list = [2, 3, 4, 1, 45, 12, 33]
count = 0
for i in range(len(my_list)):
    for j in range(0, len(my_list)):
        count = count + 1
        if my_list[i] < my_list[j]:
            temp = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = temp
print(my_list)
print(count)
# Type 3-
my_list = [2, 3, 4, 1, 45, 12, 33]
count = 0
for i in range(0, len(my_list)):
    isSwapped = False
    for j in range(0, len(my_list) - i - 1):
        count = count + 1
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            isSwapped = True
    if not isSwapped:
        break

print(f"Sorted List:{my_list}")
print(count)
