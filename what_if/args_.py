
# Topshiriq 1
def checkScore(**kwargs):
    ortacha_ball = 0
    best_subject: str = ""
    max_score = 0
    for key, value in kwargs.items():
        ortacha_ball += value
        if value > max_score:
            max_score = value
            best_subject = key
    print(f"Umumiy o`rtacha Baho:{ortacha_ball // len(kwargs.values())}")
    print(f"Eng yashi o`zlashtirgan fan: {best_subject} : {max_score}")


checkScore(ITS=4, Matematika=3, English=4, Programming=5, Web_Development=5, Enterprise=4)
