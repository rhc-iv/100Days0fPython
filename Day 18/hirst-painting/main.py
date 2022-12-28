#!/usr/bin/env python3

# import colorgram
#
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [
    (199, 158, 116), (157, 85, 39), (42, 107, 150), (132, 168, 188),
    (191, 155, 21), (10, 28, 60), (193, 142, 163), (149, 64, 93),
    (62, 24, 10), (63, 16, 36), (156, 25, 10), (194, 86, 115),
    (137, 27, 54), (131, 180, 164), (220, 202, 130), (45, 127, 96),
    (8, 102, 61), (11, 49, 33), (206, 90, 71), (222, 172, 185),
    (51, 167, 145), (19, 53, 130), (42, 162, 182), (89, 88, 8),
    (105, 120, 166), (162, 206, 198)
]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
