from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# Screen settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_BACKGROUND_COLOR = "black"

# Game settings
GAME_SPEED = 0.1

# Screen initialization
screen = Screen()
screen.title("Snake Game")
screen.bgcolor(SCREEN_BACKGROUND_COLOR)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

# Game objects initialization
snake = Snake()
food = Food()
score = Score()

# Screen events binding
screen.listen()
screen.onkey(snake.up, "u")
screen.onkey(snake.down, "d")
screen.onkey(snake.left, "l")
screen.onkey(snake.right, "r")

# Game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(GAME_SPEED)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend_tail()
        score.increase_score()

    # Detect collision with wall
    if abs(snake.head.xcor()) > SCREEN_WIDTH / 2 or abs(snake.head.ycor()) > SCREEN_HEIGHT / 2:
        game_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

# Screen exit
screen.exitonclick()
