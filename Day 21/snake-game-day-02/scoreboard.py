#!/usr/bin/env python3

from turtle import Turtle

# Instead of putting in parameters for our write() method, we'll
# create constants for both the align values and the font values &
# then just enter them in later to our write() method code:

ALIGN = "center"
FONT = ("SF Pro Display", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        # As with any integer data type where we are adding to it (
        # for our purposes here: keeping score), we want to create an
        # attribute that will store the initial 'score' value,
        # expressed as '0', and then have that variable update as the
        # score increases:

        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())

        # Because the write() method defaults to a color of black and
        # because we already have a background screen color of black,
        # we won't initially be able to see the score as it is
        # written. So we need to change the color of the Scoreboard
        # class to contrast against our background color AND we need
        # to ensure that this color change occurs BEFORE the actual
        # write() method is called:

        self.color("green")

        # Because we plan on moving the Scoreboard object to a
        # different location on the screen, we want to make sure that
        # the Turtle class default behavior of drawing its path is
        # turned off before invoking the goto() method. The penup()
        # method allows us to accomplish this:

        self.penup()

        # Finally, because the Scoreboard class is inheriting from
        # the Turtle superclass, the score display defaults to a
        # coordinate of 0,0 due to the 'center' attribute in our
        # write() method. We can use the .goto() method on the
        # Scoreboard class to cause the score to appear at the top of
        # our display so as not to interfere with playing the game.
        # Our x-axis remains the same (0) such that it remains in the
        # center along the horizontal axis, but we'll change the
        # y-axis value to move it to the top. We also want this to
        # happen BEFORE the write() method as well:

        self.goto(0, 270)

        # self.write(
        #     f"Score: {self.score}",
        #     move=False,
        #     align="center",
        #     font=("SF Pro Display", 16, "Regular")
        # )

        # Also, since the score is the only output we want to show on
        # the screen as the game is being played, we need to invoke
        # the hideturtle() method:

        self.hideturtle()
        self.update_scoreboard()

    # Since we have used the same self.write() method above and below
    # here, let's create a new function that contains this info and
    # can be called as an input in other functions:

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            move=False,
            align=ALIGN,
            font=FONT,
        )

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # We're going to create a new function that persistently checks
    # if our game is over based on the conditions that we've created
    # in our main.py file:

    # def game_over(self):

        # First, let's make it so that when the game is over & we
        # want to alert the player of the game to that fact,
        # the information gets printed in the center of the screen.
        # We'll use the goto() method to ensure this data gets
        # printed at that origin (0, 0):

        # self.goto(0, 0)

        # We can reuse the write() method here to indicate to the
        # user that is playing the game that the game is over:

        # self.write(
        #     "OH NO!\n"
        #     "GAME OVER!",
        #     align=ALIGN,
        #     font=FONT,
        #     )

    # Now we need to create a new function inside of the Scoreboard
    # class that calculates the score whenever our Snake object
    # "eats" a piece of the Food object:

    def increase_score(self):
        # This function is going to take self.score & add 1 to the
        # score total:

        self.score += 1

        # Then, we will invoke the self.write() method so that the
        # score can be updated on the game screen:

        # self.write(
        #     f"Score: {self.score}",
        #     move=False,
        #     align="center",
        #     font=("SF Pro Display", 16, "Regular")
        # )

        # Before we update the scoreboard, we need to ensure that the
        # score doesn't overwrite, graphically, the previous score.
        # Here we can use the clear() method to "clear" the previous
        # score and show the updated score:

        self.update_scoreboard()
