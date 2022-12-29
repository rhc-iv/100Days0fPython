#!/usr/bin/env python3

from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()

        # Here, we are inheriting the appearance (.shape) from the
        # Turtle class that we created earlier, but we are modifying
        # it to the "circle" attribute.

        self.shape("circle")
        self.penup()

        # We're going to use the .shapsize() method to ensure that
        # our Food is a bit smaller than the size of our Snake
        # object. We have access to this method due to our superclass
        # (Turtle) inheritance. The .shapsize() method allows us to
        # stretch both the length & the width of our object, in this
        # case our Food object. Because a normal turtle instance is
        # 20 x 20 pixels, if we give our length & width attributes a
        # value of 0.5, it will effectively half the size of our Food
        # object, resulting in a graphic that is 10 x 10 pixels:

        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

        # Let's tap into the .color() method to change the color of
        # our Food class so that it appears distinct from our Snake
        # class in the game:

        self.color("blue")

        # Let's set the .speed() of our Food class so that as soon as
        # our Snake object "eats" a piece of food, a new piece of
        # food instantly appears elsewhere on our screen:

        self.speed("fastest")

        # We now need to include our refresh(self) method so that it
        # triggers under our 'if' statement (self.head.distance) in
        # our main.py file:

        self.refresh()

    # We also need to create a new method that can be passed to our
    # main.py file so that whenever the collision detection outlined
    # by our 'if' statement there (self.head.distance) occurs,
    # the food will then move to a new place on the screen:

    def refresh(self):

        # Now we need to use the methods in the random module in
        # order to ensure that as our Snake object "eats" a piece of
        # food, the new piece of food that appears happens randomly
        # somewhere on our screen. First, let's create an attribute
        # that uses the .randint() function. This will set a boundary
        # for the Food to appear on our pre-defined screen of 600 x
        # 600 and we need to make sure that we define that boundary
        # for both the x- & y-axis of the screen. We will call it
        # 'refresh' because, in essence, it is refreshing a new
        # instance of the Food object:

        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        # Next, we will use these attributes within the .goto()
        # method in order to have each new piece of food randomly
        # appear on our screen within the boundaries set by those
        # attributes:

        self.goto(random_x, random_y)