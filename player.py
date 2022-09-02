from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("darkgreen")
        self.setheading(90)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(STARTING_POSITION)

    def move(self):
        new_x = self.xcor()
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x=new_x, y=new_y)

    def at_finish_line(self):
        y = self.ycor()
        if y >= FINISH_LINE_Y:
            return True
        return False
