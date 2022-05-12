import random
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


def random_color():
    r = random.randint(50, 255)
    g = random.randint(50, 255)
    b = random.randint(50, 255)
    color = (r, g, b)
    return color


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def extend(self):
        self.add_segment(position=self.segments[-1].position())

    def add_segment(self, position):
        segment = Turtle(shape='square')
        segment.penup()
        segment.speed('fastest')
        segment.shapesize(0.5)
        segment.color(random_color())
        segment.goto(position)
        self.segments.append(segment)

    def snake_move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
