from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
TEXT_COORD = (-200, 250)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 1
        self.goto(TEXT_COORD)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align=ALIGNMENT, font=FONT)
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
