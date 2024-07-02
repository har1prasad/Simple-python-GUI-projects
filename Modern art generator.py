from turtle import Turtle,Screen,colormode
import random

colormode(255)

jimmy = Turtle()
screen = Screen()
jimmy.shape("turtle")
jimmy.speed("fastest")

def randomcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

screen.setworldcoordinates(-10, -20, 500, 500)

def turn_left():
    jimmy.left(90)
    jimmy.forward(50)
    jimmy.left(90) 

def turn_right():
    jimmy.right(90)
    jimmy.forward(50)
    jimmy.right(90) 


def line():
    for i in range(10):
        jimmy.dot(20, randomcolor())
        jimmy.penup()
        if i != 9:
            jimmy.forward(50)
    

def grid():
    for i in range(5):
        line()
        turn_left()
        line()
        turn_right()

grid()
jimmy.hideturtle()

screen.exitonclick()