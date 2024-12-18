class Player:
    def __init__(self, name, nationality, position):
        self.name = name
        self.nationality = nationality
        self.position = position

    def run(self):
        print(f"{self.name} is running")

    def skills(self, skill):
        print(f"{self.name} : {skill} skill")

    def shoot(self, shoot):
        print(f"{self.name} : {shoot} Shoot")

    def passs(self, passed):
        print(f"{self.name} : {passed} Pass")

    def dribble(self, dribble):
        print(f"{self.name} : {dribble} Dribble")

    def header(self, header):
        print(f"{self.name} : {header} Header")

player =Player("Cristiano Ronaldo", "Portugal", "Striker")
player.run()
player.skills("Passing")
player.shoot("Heading")
player.passs("Passing")
player.dribble("Dribbling")
player.header("Heading")