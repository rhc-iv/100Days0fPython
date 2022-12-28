#!/usr/bin/env python3

# Adding methods to a class is pretty much the same as how we would
# normally define functions, except in this case the method exists
# within the class:

#     class Car:
#         def enter_race_mode():
#             self.seats = 2

# Now that we've defined a method, all we have to do to call it is
# follow the proper syntax for methods and invoke it through our object:

#     my_car.enter_race_mode()

# Let's work through this section by importing the previous code from
# the class section about the init() function:

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# When we create a method, 'self' ALWAYS has to be the first
# parameter that is defined. This is because when the method is
# called, it can understand what object called it. The 'self' keyword
# is very often used within the construction of our class but is
# rarely seen outside of it, as shown above & below.


user_1 = User("001", "Robert")
user_2 = User("002", "Jennifer")


user_1.follow(user_2)

# 'user_1' is the object; '.follow' is the method. 'user_2' is the
# input for the method.

# We can now see how the '.follow' method has worked by printing the
# 'user_1.follow' account using the attributes 'followers' and
# 'following'. We'll also print those same attributes for the
# 'user_2' account:

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# The output is as expected: there is a value of '0' for 'user_1' in
# the 'followers' output & '1' in their following output. This is
# because we used our previous method to allow 'user_1' to follow
# 'user_2'. Because 'user_2' is now followed by 'user_1', the value
# of the 'user_2' followers output is '1', but '0' for the
# 'following' attribute because we didn't invoke the method the other
# way.
