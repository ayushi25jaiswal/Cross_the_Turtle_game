from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)
        self.upward()

    def upward(self):
        self.forward(10)

    def goto_start(self):
        self.goto(0, -270)

    def is_on_finish_line(self):
        if self.ycor() >= 280:
            return True
        else:
            return False
