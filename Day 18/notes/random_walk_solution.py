#!/usr/bin/env python3

from turtle import Screen
import turtle as t
import random


tim = t.Turtle()
tim.shape("classic")
tim.pensize(15)
tim.speed("slow")
screen = Screen()
screen.bgcolor("black")


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]


for _ in range(200):
    tim.forward(20)
    tim.setheading(random.choice(directions))
    tim.color(random.choice(colours))



screen.exitonclick()
