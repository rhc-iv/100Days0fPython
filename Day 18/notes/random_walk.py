from turtle import Screen
import turtle as t
import random

tim = t.Turtle()

# Challenge 4: Random Walk

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim.shape("classic")
screen = Screen()
screen.bgcolor("black")


for walk in range(10, 51):
    tim.color(random.choice(colours))
    tim.right(random.choice(range(90, 180)))
    tim.forward(random.choice(range(10, 50)))


screen.exitonclick()