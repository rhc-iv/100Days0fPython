#!/usr/bin/env python3

# -> CLASS INHERITANCE <-
# -----------------------

# The process of inheriting behavior & appearance from an
# already-created class into a new class is known as CLASS INHERITANCE.
# Inheritance covers both appearance (attributes) and behavior (
# methods).

# Below, we've created a class called 'Animal' which has appearance (
# the num_eyes attribute) and behavior (the breathe method)

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

# Our new class, 'Fish', has some class inheritance from our previous
# class, 'Animal'. First off, the class creation syntax is to put the
# class inheritance target's name into parentheses after we type our
# new class name -> Fish(Animal):


class Fish(Animal):
    def __init__(self):

        # In order to inherit everything into the 'Fish' class from
        # the 'Animal' class, we need to ass the super().__init__
        # method inside of the initial __init__(self) method. The
        # 'super' refers to the superclass that is the parent class
        # that our new class inherits from; in this case, 'Animal' is
        # considered the superclass:

        super().__init__()

    def breathe(self):

        # We can also modify inherited appearances & behaviors by
        # again invoking the super() method. Here, we have used the
        # super() method to modify the inherited behavior of the
        # breathe() method that was previously defined in our
        # superclass, 'Animal'.

        super().breathe()

        # After the behavior inheritance has occurred, we can add
        # modifications to the inheritance. In this case, the print
        # statement will occur AFTER the inherited behavior occurs
        # because the code comes after the super() method:

        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.breathe()