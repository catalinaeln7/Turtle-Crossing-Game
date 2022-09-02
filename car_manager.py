from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_X = 310
FINISH_X = -310


class Car(Turtle):

    def __init__(self, lap_nr):
        super().__init__()
        self.shape("square")
        self.penup()
        color = random.choice(COLORS)
        self.color(color)
        self.shapesize(stretch_len=2, stretch_wid=1)
        random_y = random.randint(-250, 250)
        self.goto(x=START_X, y=random_y)
        self.speed_dist = STARTING_MOVE_DISTANCE + MOVE_INCREMENT * lap_nr

    def move(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x=x - self.speed_dist, y=y)


class CarManager:

    def __init__(self):
        self.cars = []

    def generate_car(self, lap_nr):
        car = Car(lap_nr)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move()
            if car.ycor() < FINISH_X:
                self.cars.remove(car)

    def speed_up(self, lap_nr):
        for car in self.cars:
            car.speed_dist = STARTING_MOVE_DISTANCE + MOVE_INCREMENT * lap_nr
