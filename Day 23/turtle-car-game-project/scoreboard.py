#!/usr/bin/env python3

from turtle import Turtle

FONT = ("SF Pro Display", 24, "normal")

# Detect when the turtle player has reached the top edge of the
# screem (i.e., reached the FINISH_LINE_Y). When this happens,
# return the turtle to the starting position and increase the speed
# of the cars. Hint: think about creating an attribute and using the
# MOVE_INCREMENT to increase the car speed.

# Create a scoreboard that keeps track of which level the user is on.
# Every time the turtle player does a successful crossing, the level
# should increase. When the turtle hits a car, GAME OVER should be
# displayed in the centre.


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)