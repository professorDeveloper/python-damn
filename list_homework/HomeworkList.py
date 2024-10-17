# Task1
# Remove Element from list
nums = [1, 2, 3, 4, 5, 6, 7]
nums.pop(1)
nums.pop(3)
print(nums)

# Task2 Remove Juft Element from List
nums2 = [1, 2, 3, 4, 5, 6, 7]
nums2.remove(2)
nums2.remove(4)
nums2.remove(6)
print(nums2)

# Task3
# Remove  3:5 Items from List
nums3 = [1, 2, 3, 4, 5, 6, 7]
del (nums3[3:5])
print(nums3)

# Task4
# Remove Element by index
nums4 = [1, 2, 3, 4, 5, 6]
index = 2
# nums4.remove(nums4[index])  #or
nums4.pop(index)
print(nums4)

# Task5
# Remove First Last element
nums5 = [1, 2, 3, 4, 5, 6, 7]
nums5.pop(0)
nums5.pop(len(nums5)-1)
print(nums5)

# Task6
nums6 = [1, 2, 3, 4, 5, 6, 7]
isAliveItemIndex = nums6.index(1)
nums6.clear()
nums6.append(1)
print(nums6)

# Task7
# Clear List
nums7 = [1, 2, 3, 4, 5, 6, 7]
nums7.clear()
print(nums7)

# Task 8
# Move Item To Last Position
nums8 = [1, 2, 3, 4, 5, 6, 7]
item = nums8[1]
nums8.remove(item)
nums8.append(item)

# Task 9
# reverse list items
nums9 = [1, 2, 3, 4, 5, 6, 7]
nums9.reverse()
print(nums9)
