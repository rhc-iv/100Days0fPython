#!/usr/bin/env python3

from coffeeStuff import MENU, resources

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money_profit = 0


# TODO 1. Create a report of how much water, milk, coffee, and money
#  you have used
def report(water_ingredient, milk_ingredient, coffee_ingredient,
           money_in_box):
    print("The coffee machine has:")
    print(f"Water: {water_ingredient}ml")
    print(f"Milk: {milk_ingredient}ml")
    print(f"Coffee: {coffee_ingredient}g")
    print(f"Money: ${format(money_in_box, '.2f')}")


# TODO 2. Check if resources are available for coffee order
def check_resources(user_choice, water_ingredient, milk_ingredient,
                    coffee_ingredient):
    if water_ingredient < MENU[user_choice]["ingredients"]["water"]:
        print("Sorry, not enough water!")
        return False
    if milk_ingredient < MENU[user_choice]["ingredients"]["milk"]:
        print("Sorry, not enough milk!")
        return False
    if coffee_ingredient < MENU[user_choice]["ingredients"]["coffee"]:
        print("Sorry, not enough coffee!")
        return False
    return True


def money(user_choice):
    global money_profit
    print(
        f"The cost of {user_choice} is $"
        f"{format(MENU[user_choice]['cost'], '.2f')}.\n Please insert "
        f"coins: ")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    money_total = (quarters * .25) + (dimes * .10) + (nickels * .05) + (
            pennies * .01)
    if money_total < MENU[user_choice]['cost']:
        print(
            f"Sorry, not enough money! Here is your change: $"
            f"{format(money_total, '.2f')}.")
        return False
    money_profit += MENU[user_choice]['cost']
    money_total -= MENU[user_choice]['cost']
    print(f"I have enough resources, enjoy your {user_choice}!")
    print(f"Here is ${format(money_total, '.2f')} in change.")
    return True


# TODO 3. Create user input explaining which coffee you would like to
#  order: "Espresso/Latte/Cappuccino"
coffee_machine = True

while coffee_machine:
    user_input = input(
        "What kind of coffee would you like to order? ("
        "Espresso/Latte/Cappuccino): ").lower().strip()

    if user_input == "report":
        report(water, milk, coffee, money_profit)

    elif user_input == "off":
        coffee_machine = False
        print("Goodbye!")

    elif user_input in ("espresso", "latte", "cappuccino"):
        if check_resources(user_input, water, milk, coffee):
            # TODO 4. When user selects order, ask user to insert money
            total_money = money(user_input)
            # TODO 5. Checks to make sure a drink was actually made
            if total_money:
                water -= MENU[user_input]["ingredients"]["water"]
                milk -= MENU[user_input]["ingredients"]["milk"]
                coffee -= MENU[user_input]["ingredients"]["coffee"]
    else:
        print("Invalid selection.")
