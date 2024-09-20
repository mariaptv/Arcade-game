from turtle import Turtle, Screen

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)




    def go_up(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x, y + 28)

    def go_down(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x, y - 28)