"""
Turtle Program
"""
from turtle import Turtle, Screen
from turtle_square import draw_square

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
draw_square(turtle=timmy_the_turtle)


SCREEN = Screen()

SCREEN.exitonclick()
