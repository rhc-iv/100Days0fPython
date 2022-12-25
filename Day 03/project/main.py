#!/usr/bin/env python3

# If we want to print multiple lines (or blocks) of a string,
# we use 3 ''' at the beginning & end of the print() function
# as shown below
print('''
                 _____
              .-" .-. "-.
            _/ '=(0.0)=' \_
          /`   .='|m|'=.   `-
          \________________ /
      .--.__///`'-,__~\\\\~`
     / /6|__\// a (__)-\\\\
     \ \/--`((   ._\   ,)))
     /  \\  ))\  -==-  (O)(
    /    )\((((\   .  /)))))
   /  _.' /  __(`~~~~`)__
  //"\\,-'-"`   `~~~~\\~~`"-.
 //  /`"              `      `\
//
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

# Since this is a text-based adventure game, all of our choices are
# gathered via the input() function, so let's get started. Also notice
# that in order for punctuation (especially 's) not to get parsed as
# opening or closing parts of a string, we can use the "\" character to
# "escape" them so they're ignored & just parsed by Python as plain text
# instead of part of the code.
crossroad = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" ')
crossroad_lower_case = crossroad.lower()
if crossroad_lower_case == "right":
    print("Fall into a hole. Game Over.")
elif crossroad_lower_case == "left":

    lake = str(input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. '))
    lake_lower_case = lake.lower()
    if lake_lower_case == "swim":
        print("Attacked by trout. Game Over.")
    elif lake_lower_case == "wait":

        house = str(input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? "))
        house_lower_case = house.lower()
        if house_lower_case == "red":
            print("It\'s a room full of fire. Game Over.")
        elif house_lower_case == "blue":
            print("You enter a room of beasts. Game Over.")
        elif house_lower_case == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn\'t exist. Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")
