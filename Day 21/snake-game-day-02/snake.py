#!/usr/bin/env python3

# -> CREATE SNAKE CLASS <-

# 1. We are going to place our imports here at the beginning of the
#    file for this class:

from turtle import Turtle

# 2. We are going to take the 'starting_positions' of our snake and
#    create a "constant" with it. That is, this particular tuple that
#    lives within a list is going to be accessible everywhere throughout
#    our code. Similar to import statements, we need constants to exist
#    before any of our code AND ensure that we adhere to the correct
#    syntax for constants, which is that the name that we use for
#    constants must be completely capitalized:

STARTING_POSITIONS = [
    (0, 0),
    (-20, 0),
    (-40, 0),
]

# 7. Now that we have imported our Snake class into our main.py file,
#    let's create another constant that will contain the distance our
#    snake moves while the game is running. It's important to note
#    that this & the previous constant exist so that we can make
#    changes to our code via these constants very easily. We simply
#    have to change the data in our constants to effect our code
#    instead of looking through each line of code changing variable &
#    attribute data to have some effect:

MOVE_DISTANCE = 20

# 8. We are going to create constants now that correspond to our
#    cardinal directions that our snake can move with our key presses.
#    The reason for this is that we are going to use these constants to
#    ensure that our snake isn't able to reverse its movement from any
#    direction it is moving in according to the official rules of the
#    game itself:

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):

        # 3. We're going to take our 'segments' list from our main.py
        #    file and bring it into our snake class. Also remember that
        #    whenever we are creating an __init__, we have to prepend
        #    each part of the nested code with the 'self' keyword & join
        #    it using a "." character:

        self.segments = []

        # 4. Next, we are going to create a method called
        #    'create_snake()'. We are also going to create another
        #    method called 'self.head' that will ensure that we can
        #    enumerate an item from the 'self.segments' list, in this
        #    case, the first (0) segment:

        self.create_snake()
        self.head = self.segments[0]

    # 5. Now we need to define our create_snake method by bringing our
    #    main.py code where we made the snake & nest it inside this new
    #    method. We need to change 'starting_positions' into
    #    'STARTING_POSITIONS' in order to ensure that we are using our
    #    constant created at the beginning of this file. We also need to
    #    do a turtle module import, which we've done again at the top of
    #    this file. Finally, in order to refer correctly to our
    #    attributes 'segments', we have to prepend the
    #    'segments.append' portion of our code with the 'self' keyword:

    def create_snake(self):
        for position in STARTING_POSITIONS:

            # Since we've created a new 'add_segment' function below,
            # we can simply call that function in our 'create_snake'
            # function instead of re-writing or pasting in the code
            # again:

            self.add_segment(position)

    # 6. Next we need to create another method, called 'move', that will
    #    encapsulate our code from main.py where we defined how our
    #    snake segments should move in unison. Again, because we are
    #    working inside our class and the __init__ for that class,
    #    we must prepend every instance of 'segments' with the 'self'
    #    keyword. We can also replace our .forward distance,
    #    enumerated as 20 from our previous code, with our
    #    MOVE_DISTANCE constant:

    # 9. We need to create a way for our snake to "grow" or add
    # segments to its size each time it consumes one of the Food
    # objects. This behavior comports with how the original Snake
    # Game worked. We're going to do that by creating  new function
    # within our Snake class that does just that! First, we need this
    # function to act upon the position of our Snake object at any
    # given time that it "eats" a piece of food, so we include
    # 'position' in our function parentheses. Next, we copy & paste
    # our 'new_segment' code for our 'create_snake' object & add it
    # to our 'add_segment' function. Now that the 'add_segment'
    # function has been created & will be able to be called as an
    # input in other functions, we're going to follow it with another
    # created function called 'extend' which will address increasing
    # the size of our Snake object based on the condition of it
    # "eating" food in-game. The position within 'add_segment'
    # function inside of 'extend' is going to get the last position
    # of our Snake object by referencing the segments list in the
    # Snake class and using -1, which is the way in Python that we
    # can always access the last item within a list. By appending the
    # position() method from the turtle module, we are going to be
    # able to pinpoint that last segment's exact position:

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(x=position[0], y=position[1])
        self.segments.append(new_segment)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, -1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Next, we need to create functions (or methods since we are
    # associating them with a class per OOP standards) for the snake
    # movement as we wish for it to be controlled by key presses and
    # as stated in our .onkey() methods in our main.py file. From
    # there, we are going to take our lead segment from our
    # self.segments list, using 0 per Python's iteration of list
    # items, then we are going to make each that correspond to our
    # key press directions and use the .setheading() method to
    # indicate the heading of the snake. The setheading() method
    # takes an integer or float as an attribute and represents the
    # angle that the instance needs to move along. However, since
    # we've already defined these angles in our file's constants,
    # we are instead going to insert the constant name instead of an
    # actual value expressed as an integer. In addition, we are going
    # to use 'if' statements to ensure that whatever heading our
    # snake is currently on, it won't be able to stop & go in the
    # reverse direction as this contravenes the rules of the Snake
    # game:

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
