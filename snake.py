from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:
    def __init__(self):

        self.snake = []
        self.create_snake()
        self.snake_head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_part(position)

    def move(self):
        for part_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[part_num - 1].xcor()
            new_y = self.snake[part_num - 1].ycor()
            self.snake[part_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def add_part(self,position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.snake.append(new_turtle)

    def extend(self):
        self.add_part(self.snake[-1].pos())

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def reset(self):
        for part in self.snake:
            part.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.snake_head = self.snake[0]