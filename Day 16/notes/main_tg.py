#!/usr/bin/env python3

# The "Turtle Graphics" CLASS actually resides within a module in our default
# installation of Python. Thus, we need to import it just as we would with any
# other module:

#   import turtle

# Next, we can access the Turtle class by invoking it once the import is 
# complete. Whenever we type 'turtle' into our development environment, we
# should get a dropdown-menu that will show us all of the classes, objects,
# functions, dictionaries, lists, and variables contained within the "Turtle
# Graphics" module (or by another name, library). We are able to call this menu
# by appending a "." to the turtle keyword. Also, we need to remember that in
# order to begin construction of an object, we have to add parentheses at the
# end of the class. We also need to name our object; this is done (as shown in
# the constructing_objects.py file in this directory) by adding our object name
# just as we would with a variable:

#   timmy = turtle.Turtle()

# So we have created an OBJECT('timmy') and we have told Python that this
# object is going to be constructed within the CLASS 'Turtle'. We know that
# 'Turtle" is a class not only because of it being indicated as one in the menu
# we accessed on invoking the 'turtle' module, but also because it is
# capitalized in the PascalCase format which is the standard for classes in
# Python syntax.

# We can save ourselves a little time if we know what parts of the "Turtle
# Graphics" module/library we plan on using to create objects. This can be done
# via our import statement by specifying that part of the module/library like
# so:

from turtle import Turtle, Screen

# Now that we hae imported the 'Turtle' CLASS, we can invoke it directly in our
# object-construction like this:

timmy = Turtle()

# If we print our object to the console:

print(timmy)
timmy.shape("turtle")
timmy.color("cornsilk4")
timmy.forward(100)

# ...the output in our console would resemble this:

#     <turtle.Turtle object at 0x123a45678>

# This output in the console simply means that we have executed a print() 
# function that calls the object & where, as noted by the random string/integer
# portion, our computer has stored that object in its memory.

# We can begin construction of the 'timmy' object by specifying its attributes.
# This is done following Python syntax which involves inserting a "." between
# the OBJECT and the ATTRIBUTE. In much the same way that we called the
# dropdown menu earlier from the 'turtle' module, this "." will create another
# menu that gives us access to all the attributes available to us when making
# an object that the parent class ('Turtle') offers. For this exercise, we also
# want to use another class from the 'turtle' module called "Screen", which has
# attributes related to the screen size, position and location of the screen
# that we plan on using the "Turtle Graphics" on. Remember that importing 
# multiple parts of a library is done after the 'from/import' statement and
# that Python uses a comma-separated syntax for this purpose. Note above that
# we have called the 'Screen' class along with the 'Turtle' class in the import
# statement:

my_screen = Screen()

# Here we've created another object called 'my_screen' and will use the
# "Screen" class to construct this new object and call the 'canvheight'
# attribute to begin building our object:

my_screen.canvheight
print(my_screen.canvheight)

# As with our 'timmy' object, if we wrapped our 'my_screen' object within a
# print() function, the output shown would be:

#    300

# This output is shows the screen height (canvheight) of the 'my_screen' object
# and simply printed those dimensions to our console. Also notice that upon
# running the .py file, almost simultaneously with the console output, we see
# a momentary second 'screen' flash up on our computer screen.

# Now that we have a baseline understanding of ATTRIBUTES when attempting to
# construct an OBJECT, let's now move to examining how to attach METHODS to our
# objects. They syntax for methods is the same as the syntax for attributes; we
# insert a "." between the object and the method. But, since methods  are 
# functions that will live within our objects, we need to append a set of
# parentheses to the method in order to 'activate' it. And, like attributes, 
# the insertion of the "." character will also call a dropdown menu that we can
# access in the class that we want to use:

my_screen.exitonclick()

# The above method that we've bound to our object (and selected from the 
# dropdown menu) will make it such that the window called by the print() 
# function previously will not display briefly, but rather it will display up
# until we use our cursor to 'click' on that window (thus the 'exitonclick'
# moniker). Also, until that window is closed, the program will continue to run
# as it awaits some sort of input from the user.

# If we return to our initial print statement:

#     print(timmy)

# ...we can perform built-in function upon the 'timmy' object that are
# available to use from the module that we imported. Let's change the 'shape'
# of the graphic that appears on our pop-up window. When we run our code, the
# initial image is simply a right-facing arrow. We're going to alter our print
# statement using the shape() function in order to change the image shape to
# that of a turtle --> timmy.shape("turtle") We're also going to use another
# function from that module called 'color()' to change the color of the image
# and use a string value of "cornsilk4".

# As another exercise, let's cause the turtle in our window to 'move'. The
# documentation for the "Turtle Graphics" module has a method called forward()
# that takes as an argument a number (integer or float) & will cause the image
# the method is acting upon to move in the window. The number we entered is
# considered a unit of 'distance'. Our exercise calls for us to move the turtle
# forward by a 'distance' of 100, thus the method will be written:

#     timmy.forward(100)