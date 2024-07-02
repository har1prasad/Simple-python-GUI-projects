from turtle import Turtle, Screen

jimmy = Turtle()
screen = Screen()


def move_forward():
    jimmy.forward(10)


def move_backward():
    jimmy.backward(10)


def move_right():
    jimmy.right(10)


def move_left():
    jimmy.left(10)


screen.listen()
screen.onkeypress(fun=move_forward, key='w')
screen.onkeypress(fun=move_backward, key='s')
screen.onkeypress(fun=move_right, key='d')
screen.onkeypress(fun=move_left, key='a')
screen.onkeypress(fun=screen.resetscreen, key='c')

screen.exitonclick()
