#!/usr/bin/env python3

# Following on for our previous instruction and code where we learned
# to create a class, we'll continue by learning how to create
# attributes for that class. First, let's copy our previous code into
# this file:

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

# If we want to create an attribute that has a default value that we
# expect to be the same across all objects in that class, we can
# define it like a variable AND it will populate whenever we call our
# init() function such that we don't have to ender it in to each of
# the objects as we've done below with the user_id and username.
# Let's add another attribute, 'followers' with a default value of 0
# in our init() function above. Also, because we've created this
# default value for this specific attribute, we do not have to
# include it as a parameter within the init() function parentheses as
# it isn't parsed by Python as a required positional argument. That
# is, the initialization will always be the value we've defined.
# Our 'user_id' and 'username' parameters require values not set at
# initialization, so they require input whereas 'followers' does not
# since it will ALWAYS be '0' (or the value we give it).


# At this point, the Python interpreter expects that '__init__' is a
# function call where we will initialize our starting attributes for
# the User class. Also, everytime we create a new object from the
# class that contains the init() function, that init() function will
# be called. The init() function can also have as many parameters as
# we want to associate with it. The 'self' parameter is simply a
# Pythonic reference to the object that we are constructing. So now
# that we have our init() function added to our code, let's create
# some parameter to add to it. Let's pass the 'id' and 'username'
# attributes to the init() function in order to create our initial
# values. 'self.id' is going to be an attribute that's associated
# with this User class and we can set it to 'user_id' whose value
# will get passed to it anytime when a user gets constructed.


user_1 = User("001", "robert")

# Now that we've used the init() function to add the 'user_id' attribute
# to our object, we can pass the data to the attribute within the
# parentheses of the User class and, due to the init() function,
# this data will be initialized at the beginning of the program.We've
# also added another attribute, 'username', which will behave in the
# same way. Also, whatever parameters we create within the init()
# function, MUST be passed to our class whenever it is called. These
# are also known as REQUIRED POSITIONAL ARGUMENTS.

# Using attributes within a class is as simple as taking our object (
# in this case, 'user_1') and then inserting a "." character in order
# to access attributes within that class from the dropdown menu:

#   user_1.id = "001"
#   user_1.username = "robert"

# In the above example, neither 'id' or 'username' were specified as
# attributes in the dropdown menu. But because we used the proper
# syntax, we have created our own attributes that will now be added
# to the class whenever we call on them thru our objects. Remember
# that attributes within classes are akin to variables, so we have
# the freedom to not only name them, but to also define (and store)
# them. Once we've accomplished this, those attributes will then
# become available thru Python's dropdown menu.

# What if we wanted to have multiple attributes available for our
# objects upon the start of our code? What can we do via Python in
# order to have a 'default' set of attributes assigned to any object
# that we create? In Python, we do this via a CONSTRUCTOR. The
# constructor is the part of a class that allows us to specify what
# should happen when our object is created. In programming, this is
# generally called INITIALIZING: this sets the values of anything
# that can have values in Python (variables, attributes, objects,
# etc) to a set of STARTING VALUES at the beginning of a program.

# In Python, this constructor is implemented via a special function
# known as 'init()'. The syntax for this function is also different
# from what we've previously learned. See below:

#     class User:
#         def __init__(self): <-- This initializes attributes

# Notice that the init() function is preceded & proceeded by 2
# underscores before & after the function. Let's revisit the code
# above and set an init() function within our new object.


user_2 = User("002", "jennifer")


print(user_1.id, user_2.id)
