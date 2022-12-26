#!/usr/bin/env python3

# Calculator Project

# Create imports for ASCII art and the 'os' module
# in order to construct a clear() function:
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

from art import logo

# Create functions for each of the mathematical functions
# that we are going to include in the calculator:
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

# Create a dictionary, to be referenced later on in
# our calculator app that contains strings for our
# mathematical operands as well as our functions that
# were defined above:
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Create a 'calculator' function that will encompass
# all of our operations, including function calls for
# our math functions and print the app logo upon starting
# the calculator (and any subsequent uses of the calculator
# after we have cleared the console):
def calculator():
    print(logo)

# Create an input that will ask the user to enter a number,
# convert that input to a float, then print a list of the
# mathematical operands available to the user after the 
# first input is entered:
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

# Create a boolean variable that, when TRUE, will allow for
# further inputs to be entered:
    should_continue = True

# Use a 'while' loop to trigger when the should_continue
# condition is TRUE:
    while should_continue:

# Create input variables for the mathematical operand chosen
# by the user as well as the second number input (again,
# converted to a float).)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

# Create variables that contain the number(input) variables as
# well as the mathematical operation desired then derive an 
# answer from that calculation:
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

# Create a print statement, with multiple F-Strings, to construct
# our output to the user which will show an inline calculation
# of their inputs:
        print(f"{num1} {operation_symbol} {num2} = {answer}")

# Use an 'if/else' statement to offer the user an opportunity
# to add further input to the answer of their original calculation.
# Use the 'else' statement to dictate the behavior of the app
# if the user wants no further input to be taken:
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()

# Perform a function call on the calculator() function that
# we created.
calculator()
