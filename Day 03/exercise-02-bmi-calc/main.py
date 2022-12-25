#!/usr/bin/env python3

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# We create/store a variable that is the mathematical
# operation needed to calculate BMI, then we create/store
# another variable that takes that calculation and creates
# an integer that is rounded.
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(round(bmi))

# Now, we need to use 'if/else'/'elif' statments to check
# the calculated BMI value & determine which range that value
# falls in via the boolean result.

# First, we open with an initial 'if' statement, which
# corresponds to the first category of any BMI that is
# calculated below (less than) 18.5. If the value is TRUE,
# the print() function occurs.  If it is FALSE, the 
# follow-on 'elif' statment is checked.
if bmi_as_int < 18.5:
        print(f"Your BMI is {bmi_as_int}, you are underweight.")

# If this 'elif' is checked based on a previous boolean return
# of FALSE, it will calculate whether or not the calculated
# BMI value is below (less than) 25. Because the opening 'if'
# statement checked if BMI is below 18.5, this 'elif' also checks
# if the BMI is 18.5 or greater (up to the comparison operator
# that is listed; in our case, 25.)  If this 'elif' is TRUE, the
# print() function will occur.  If FALSE, Python will move on to
# the next 'elif' statement.
elif bmi_as_int < 25:
        print(f"Your BMI is {bmi_as_int}, you have a normal weight.")

# As above, this 'elif' statement checks the boolean value of the
# BMI calculation between 25 and 29. It does not check 30 because
# there is no "=" comparison operator in the 'elif'. TRUE results
# in the print() function and FALSE moves to the next 'elif'
# statement.
elif bmi_as_int < 30:
        print(f"Your BMI is {bmi_as_int}, you are slightly overweight.")

# Our final 'elif' statment checks the BMI calculation with a 
# range from 30 to 34. All previous rules apply here.
elif bmi_as_int < 35:
        print(f"Your BMI is {bmi_as_int}, you are obese.")

# Finally, we must "close" the opening 'if' statement with a
# corresponding 'else' statment. Since the last range of BMI
# calculations ended at 34 (given the  previous comparison
# operator in the above 'elif'), this 'else' statement is TRUE if the BMI is over
# 35, then triggers the print() function. Any previous 'if' or
# 'elif' statment that parses as TRUE make this else statement
# FALSE.
else:
        print(f"Your BMI is {bmi_as_int}, you are clinically obese.")