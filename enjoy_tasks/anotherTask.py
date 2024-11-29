list = []
for i in range(1, 6):
    for j in range(1, 6):
        list.append(0)
while True:
    print("a -> Show Place")
    print("b -> Left Place")
    print("c -> Exit Place")
    num = input("Enter your choice:")
    if num == "a":
        index = 0
        for i in range(1, 6):
            for j in range(1, 6):
                print(list[index], end=' ')
                index = index + 1
            print("")

        placeNum = int(input("Joy Raqami:"))
        if placeNum < len(list) and placeNum > 0:
            if list[placeNum - 1] == 0:
                carname=input("Enter your carname:")
                list[placeNum - 1] = carname
                print("Moshina Qoyildi ! \n")
            else:
                print("Moshina Bor ! \n")
        else:
            print("Nomalum joy raqami ! \n")
    elif num == "b":
        index = 0
        for i in range(1, 6):
            for j in range(1, 6):
                print(list[index], end=' ')
                index = index + 1
            print("")

        placeNum = input("Mashina Nomi:")
        list[list.index(placeNum)]=0
        print("Moshina Olb chiqb ketildi ! \n")


    elif num == 'c':
        print("Car Place dan chiqdingiz ! ")
        break
    else:
        print("Invalid Choice\n")