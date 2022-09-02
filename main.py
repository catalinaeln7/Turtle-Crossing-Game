import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossy road")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

loop_counter = 0
lap_nr = 0

screen.listen()
screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Getting to finish line
    if player.at_finish_line():
        lap_nr += 1
        player.refresh()
        car_manager.speed_up(lap_nr)
        scoreboard.refresh()

    # Generating car every 6 loops
    if loop_counter % 6 == 0:
        car_manager.generate_car(lap_nr)

    # Detect collision with car
    # TODO
    for car in car_manager.cars:
        if car.ycor() - 20 <= player.ycor() <= car.ycor() + 20 and player.distance(car) < 35:
            game_is_on = False
            scoreboard.game_over()

    car_manager.move_cars()
    loop_counter += 1

screen.exitonclick()
