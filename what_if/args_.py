
# Task 1
def checkScore(**kwargs):
    ortacha_ball = 0
    max_score = 5
    good_subject ={}
    for key, value in kwargs.items():
        ortacha_ball += value
        if value >= max_score:
            max_score = value
            good_subject[key] = value

    print(f"Umumiy o`rtacha Baho:{ortacha_ball // len(kwargs.values())}")
    print(f"Eng yashi o`zlashtirgan fan: {good_subject}")


checkScore(ITS=4, Matematika=3, English=4, Programming=5, Web_Development=5, Enterprise=4)
