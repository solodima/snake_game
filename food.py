from turtle import Turtle
import random
from snake import random_color


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.3, 0.3)
        self.random_color()
        self.speed('fastest')
        self.refresh()

    def random_color(self):
        self.color(random_color())

    def refresh(self):
        self.random_color()
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
