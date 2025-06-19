from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.initiation(x, y)

    def initiation(self, x, y):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x,y)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.x, new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.x, new_y)

