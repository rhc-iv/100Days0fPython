#!/usr/bin/env python3
from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color_1():
    r = random.randint(101, 255)
    g = random.randint(101, 255)
    b = random.randint(101, 255)
    color = (r, g, b)
    return color

def random_color_2():
    r = random.randint(0, 100)
    g = random.randint(0, 100)
    b = random.randint(0, 100)
    color = (r, g, b)
    return color


# Challenge 5: Create a Spirograph


for _ in range(0, 360):
    t.left(90)
    t.shape("turtle")
    t.pencolor(random_color_1())
    t.fillcolor(random_color_2())
    t.width(1)
    t.speed("fastest")
    t.left(1)
    t.circle(100)


screen = Screen()
screen.exitonclick()
