#!/usr/bin/env python3

# In OOP, we strive to create objects, which are models for some part of our
# code that has a relationship to other parts of our code but that also has an
# independent function in our program.

# When we think about our approach to these models, it's a good practice to
# define that model by 2 criteria:

#   What the model has.
#   What the model does.

# Another way to properly give names to the idea of 'has' and 'does' is to
# think of them (respectively) as 'attributes' and 'methods'. If, for example
# we were making a model that replicated a waiter in a restaurant, we might
# begin to create that model in this way:

#   WAITER(class)
#   Has (attributes):
#       is_holding_plate = True
#       tables_responsible = [4, 5, 6]
#   Does:
#       def take_order(table, order):
#       # Takes order to Chef
#       def take_payment(amount):
#       # Add money to restaurant

# An ATTRIBUTE is a variable that is associated with a modeled object. In the
# above example, our CLASS  would be the "waiter". A METHOD is simply a
# function that a modeled object can do. Remember that in OOP, we are trying to
# create models that mimic real-life objects and we use methods and attributes
# to accomplish this. The things that our OBJECTS HAVE are modeled with
# variables and the things that our OBJECT DO are modeled with functions. A
# CLASS is the complete model that we've created and the collection of 
# variables and attributes within the class are known as OBJECTS.

# In Python, we can also create MULTIPLE VERSIONS of the same object that can
# be grouped within the same class. 