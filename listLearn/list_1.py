
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1.isdigit() & num2.isdigit():
            (num1, num2) = (int(num1), int(num2))
            return num1 + num2


list = [2, 1, 5, 4, 3]

print(list[0])  # 1
print(list[4])  # 5

list.insert(10, 100)
print(list)


list.pop(4)


print(list.sort())


#task1

fruits = ["apple","banana","cherry","date","elderberry"]

fruits.pop(2)
fruits.pop(3)
print(f"fruits: {fruits}")


#task2
nums =[1,2,3,4,5,6,7,8,9]
nums.remove(2)
nums.remove(4)
nums.remove(6)
nums.remove(8)
print(nums)