#!/usr/bin/env python3

# --- Creating Classes in Python ---

# The syntax for creating our own classes is simple. It must begin
# with the 'class' keyword followed by the class name, then a colon
# is inserted at the end of the class name. Remember too that all
# class names must use PascalCase in their creation; each word in the
# class name must be capitalized:

#     class MyClass:

# All of the code that we write to construct the class will then be
# indented beneath the class/class name declaration. Let's create an
# example. Suppose that we have a website, and we want to create a
# class that models the users of our website; from what they have and
# what they can do when visiting our website.

class User:
    pass


# For now, let's leave the class empty. But let's also make note of
# the fact that because the class has been created, we can access
# that class in order to create our first user object. Remember that
# to initialize the class when we are constructing objects, it is
# necessary to add a set of parentheses to the class that we are
# using for our object:

user_1 = User()

# At this point, PyCharm is indicating that there is still an error
# in our class construction; that is, it expects an indented block of
# code to follow the class declaration. This protocol (and the error
# message that it generates) is true for any line of code that is
# typically followed by indented code. For instance, this error will
# pop up with functions or 'if' statements if no indented code
# follows it. We can, however, use the PASS keyword where Python
# expects that indented code to stop these error messages. The only
# caveat is that 'pass' should be indented itself to correct the
# error. Let's add the 'pass' keyword to our User class above  to
# remedy this error message.
