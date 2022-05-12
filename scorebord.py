from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')
POSITION = (0, 260)
COLOR = 'white'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(POSITION)
        self.ht()
        self.penup()
        self.color(COLOR)
        self.update_scoreboard()
        self.speed('fastest')

    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Питон убился! Гамовер.", False, align=ALIGNMENT, font=FONT)
