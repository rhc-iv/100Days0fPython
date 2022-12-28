#!/usr/bin/env python3

from turtle import Screen
import turtle as t
import random

tim = t.Turtle()

colors = ["black", "slate gray", "royal blue", "midnight blue",
          "dark slate gray", "dark olive green", "saddle brown",
          "dark red", "purple", "indigo"]

tim.shape("classic")
tim.color("black")


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.left(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

# for _ in range(3):
#     tim.speed(1)
#     tim.pencolor("azure4")
#     tim.left(120)
#     tim.forward(50)
#
# for _ in range(4):
#     tim.speed(1.2)
#     tim.pencolor("burlywood4")
#     tim.left(90)
#     tim.forward(50)
#
# for _ in range(5):
#     tim.speed(1.4)
#     tim.pencolor("DarkGray")
#     tim.left(72)
#     tim.forward(50)
#
# for _ in range(6):
#     tim.speed(1.6)
#     tim.pencolor("DarkOrange4")
#     tim.left(60)
#     tim.forward(50)
#
# for _ in range(7):
#     tim.speed(1.8)
#     tim.pencolor("DimGrey")
#     tim.left(51.4285714286)
#     tim.forward(50)
#
# for _ in range(8):
#     tim.speed(2.0)
#     tim.pencolor("goldenrod4")
#     tim.left(45)
#     tim.forward(50)
#
# for _ in range(9):
#     tim.speed(2.2)
#     tim.pencolor("gray20")
#     tim.left(40)
#     tim.forward(50)
#
# for _ in range(10):
#     tim.speed(2.4)
#     tim.pencolor("HotPink4")
#     tim.left(36)
#     tim.forward(50)

screen = Screen()
screen.exitonclick()
