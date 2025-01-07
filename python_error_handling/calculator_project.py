def add():
    inputNum()
    print(f"{num1} + {num2} = {num1 + num2}")


def ayriuv():
    inputNum()
    print(f"{num1} - {num2} = {num1 - num2}")


def inputNum():
    global num1
    global num2
    while True:
        try:
            num1 = int(input("Birinchi raqam: "))
            num2 = int(input("Ikkinchi raqam: "))
            break
        except Exception as e:
            print("Son raqam kiriting")


def bolish():
    inputNum()
    try:
        print(f"{son1} / {son2} = {son1 / son2}")
    except ZeroDivisionError:
        print("Sonni 0 ga bo`lish mumkin emas !")


def kopaytirish():
    inputNum()
    print(f"{son1} * {son2} = {son1 * son2}")


son1 = 0
son2 = 0
while True:
    print("1-Plus")
    print("2-ayiruv")
    print("3-Bo`lish")
    print("4-Ko`paytirish")
    print("5-Chiqish")
    try:
        choice = int(input("Tanlovni kiriting: "))
        if choice == 1:
            add()
        elif choice == 2:
            inputNum()
            ayriuv()
        elif choice == 3:
            inputNum()
            bolish()
        elif choice == 4:
            inputNum()
            kopaytirish()
        elif choice == 5:
            break

    except Exception:
        print("""Tanlovni to'g'ri kiritdingiz !""")
