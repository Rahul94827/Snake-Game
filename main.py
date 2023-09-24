from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.title("Snake Game")
screen.setup(width=600,height=600)
screen.tracer(0)
screen.bgcolor("Black")

snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

flag=True
while flag:
    screen.update()
    time.sleep(0.1)

    #Detect collision with food
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with the wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.reset()
        snake.reset()



    #Dectect collision with the body
    for segment in snake.segment[1:]:
        if segment==snake.head:
            pass

        elif snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
