blueprint == class

car = CarBlueprint()

# Waiter
has == attributes (data)
is_holding_plate = True
tables_responsible = [4, 5, 6]

does == methods (function)
def take_order(table, order):
  # take order

def take_payment(amount):
  # add money

  import turtle

#object       #class
timmy = turtle.Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# PrettyTable

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Ticker name", ["TSLA", "NVDA", "GOOGL"])
table.add_column("Description", ["Tesla", "NVIDIA", "Google"])
table.align["Description"] = "l"

print(table)

Project - Coffee Machine

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}):  ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
