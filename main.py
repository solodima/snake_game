from turtle import *
from snake import *
import time
from food import *
from scorebord import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Погоняй питона")
screen.tracer(0)
colormode(255)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    # Detect collision with food
    if snake.head.distance(food) < 9:
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 9:
            scoreboard.game_over()
            game_on = False

    if snake.head.xcor() > 285 or snake.head.xcor() < -299 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.game_over()
        game_on = False


screen.exitonclick()
