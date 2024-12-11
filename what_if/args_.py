# Task 1

def middleScore(kwargs: dict):
    ortacha_ball = 0
    for key, value in kwargs.items():
        ortacha_ball += value
    print(f"Umumiy o`rtacha Baho:{ortacha_ball // len(kwargs.values())}")


def topSubject(kwargs: dict):
    max_score = 5
    good_subject = {}
    for key, value in kwargs.items():
        if value >= max_score:
            max_score = value
            good_subject[key] = value
    print(f"Eng yashi o`zlashtirgan fan: {good_subject}")


def pastSubject(kwargs: dict):
    min_score = 3
    bad_subject = {}
    for key, value in kwargs.items():
        if value <= min_score:
            bad_subject[key] = value
            min_score = value
    print(f"Eng past o`zlashtirgan fan: {bad_subject}")


def checkScore(**kwargs):
    while True:
        print("1-O`rtacha Hisob")
        print("2-Yaxshi o`zlashtirgan Fanlar")
        print("3-Eng past o`zlashtirgan fanlar")
        print("4-Chiqish")
        chose = int(input("Choose:"))
        if chose == 1:
            middleScore(kwargs)
        elif chose == 2:
            topSubject(kwargs)
        elif chose == 3:
            pastSubject(kwargs)
        elif chose == 4:
            print("Done !")
            break
        else:
            print("Invalid Choice")


checkScore(ITS=4, Matematika=3, English=4, Programming=5, Web_Development=5, Enterprise=4)
