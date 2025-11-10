from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from bonus_food import BonusFood

screen = Screen()
screen.title("***Python Snake Game***")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off automatic screen updates

game_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()
bonus_food = BonusFood()
bonus_food.deactivate() # Initially hide bonus food
food_ate_count = 0

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect collision with food
    if food.active and snake.head.distance(food) < 15:
        # print("Nom Nom Nom")
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()
        food_ate_count += 1
        
        # Activate bonus food every 5 regular foods eaten
        if food_ate_count % 5 == 0:
            bonus_food.activate()
            food.hide()
    
    if bonus_food.active and snake.head.distance(bonus_food) < 15:
        bonus_food.deactivate()
        food.show()
        for _ in range(2):  # Extend snake by 2 segments for bonus food
            snake.extend_snake()
        scoreboard.increase_score(points=5)  # Increase score by 5 for bonus food
    
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()
        
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()