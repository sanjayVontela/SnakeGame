from turtle import Screen
import food
import snake
import scorecard
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
score = scorecard.Scorecard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.snake_head.xcor() >300 or snake.snake_head.xcor() <-300 or snake.snake_head.ycor() >300  or snake.snake_head.ycor() <-300:
        score.reset()

        snake.reset()

    for part in snake.snake:
        if part != snake.snake_head and snake.snake_head.distance(part)<5:
            score.reset()
            snake.reset()


screen.exitonclick()