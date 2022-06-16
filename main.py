from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(800,800)

colors = ["red", "yellow", "orange", "blue", "green"]
start_positions = [ -50, 0, 50 , 100, 150 ]
all_turtles = []
start_positions_counter = 0
choice1 = ''
finish_position = 360.00
winner = ''

selection = "bad"
while (selection == 'bad'):
    choice1 = raw_input("Choose/Bet on a turtle color of choice")
    if choice1 not in colors:
        print("Choose allowed colors turtle only in choices")
    else:
        selection = "good"


if selection == "good":
    for color in colors:
        my_turtle = Turtle('turtle')
        my_turtle.color(color)
        my_turtle.penup()
        my_turtle.goto(x = -370, y= start_positions[start_positions_counter])
        start_positions_counter += 1
        all_turtles.append(my_turtle)


def start_race():
    destination = True
    while destination :
        for turtle in all_turtles:
            random_move = random.randint(10,40)
            turtle.forward(random_move)
            if turtle.xcor() > finish_position:
                destination = False
                winner = turtle.color()
                print("The winner is : {0}".format(winner[0]))
start_race()
screen.exitonclick()