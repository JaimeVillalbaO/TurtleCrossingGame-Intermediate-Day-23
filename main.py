import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=500)
screen.tracer(0)
jaime = Player()
screen.listen()
screen.onkeypress(jaime.move_turtl, 'Up')
car_manager = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # detect collision with a car

    for car in car_manager.all_cars: 
        if car.distance(jaime)<20:
            score.game_over()
            game_is_on = False
    
    # detect sussecful cross
    if jaime.is_at_finish():
        car_manager.level_up()
        score.score_up()
        
    
        
screen.exitonclick()
