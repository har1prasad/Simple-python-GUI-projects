from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "blue", "green", "yellow", "brown"]
y_pos = [150, 75, 0, -75, -150]
turtles = []
is_race_on = False

for turtle_index in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    turtles.append(new_turtle)

user_input = screen.textinput("Make your bet", "Which turtle will win the race? (Enter a color):").lower()

if user_input is not None:
    is_race_on = True

while is_race_on:

    for turtle in turtles:

        if turtle.xcor() > 240:
            is_race_on = False
            win_color = turtle.pencolor()
            if user_input == win_color:
                print(f"you've won, the {win_color} turtle is the winner!")
            else:
                print(f"you've lost, the {win_color} turtle is the winner!")

        turtle.forward(random.randint(a=0, b=10))

screen.exitonclick()
