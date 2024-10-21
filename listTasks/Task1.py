nums = [2, 3, 4, 5, 1, 6, 7]

nums.sort()
engKattaSon = nums[len(nums) - 1]
print(f"Listdagi Eng katta son :{engKattaSon}")

# Task2
nums = [2, 3, 4, 5, 1, 6, 7]
nums.sort()
engKichikSon = nums[0]
print(f"Listdagi Eng kichik son :{engKichikSon}")

# Task3
nums = [2, 3, 4, 5, 6, 6]
print(f"Orginal list :{nums}")

number = int(input("Enter a number: "))
nums.insert(len(nums) // 2, 1)
print(nums)

# Task4
nums = [2, 4, 5, 6, ]
number = int(input("Enter n:"))
nums.append(number)

# Task5
nums = [2, 4, 5, 6, 7]
firstItem = int(input("Birinchi element:"))
endItem = int(input("Oxirgi element:"))
nums.insert(0, firstItem)
nums.append(endItem)
pos = len(nums) - 2
newList = nums[0:2]
newList.extend(nums[pos:])

print(newList)

# task 6
nums = [1, 2, 3, 5, 6, 7, 8, 9]
yigindi = nums[0] + nums[1] + nums[2] + nums[3] + nums[4] + nums[5] + nums[6] + nums[7]
print(nums.index(3))

# to`liq yig`indi =45
print(f"Tushib qolgan son :{45 - yigindi}")
