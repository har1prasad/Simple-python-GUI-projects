from turtle import Turtle,Screen
import random

jimmy = Turtle()
jimmy.shape("arrow")
jimmy.speed(0)
jimmy.pensize(1)

def randomcolor():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

size_of_gap = 3 #It should be atleast one

for i in range(int(360 / size_of_gap)):
    jimmy.color(randomcolor())
    jimmy.circle(100)
    jimmy.setheading((jimmy.heading() + size_of_gap))

screen = Screen()
screen.exitonclick()