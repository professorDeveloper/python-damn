students_count = int(input("Darsda qatnashgan talabalar soni:"))
students_name = []
students_rank = []
students_sort_rank = []
for i in range(1, students_count + 1):
    name = input(f"{i}-talaba ismi:")
    rank = input(f"{i}-talaba bali:")
    students_name.append(name)
    students_rank.append(rank)
for i in range(students_count):
    for j in range(0, students_count-i-1):
        if students_rank[j] < students_rank[j+1]:
            temp = students_rank[j]
            students_rank[j] = students_rank[j+1]
            students_rank[j+1] = temp
            temp_name = students_name[j]
            students_name[j] = students_name[j+1]
            students_name[j+1] = temp_name

for i in range(students_count):
    print(f"Talabalar {students_rank[i]} bali {students_name[i]}")

12