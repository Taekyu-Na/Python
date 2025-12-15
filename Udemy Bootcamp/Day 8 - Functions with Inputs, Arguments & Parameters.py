More Functions

def greet():
    print("Hello")
    print("I am")
    print("TK")

greet()

# Function with Input
def greet_with_input(name):
    print(f"Hello {name}")
    print(f"I am {name}")
    print(name)

name = input("What is your name? ")
greet_with_input(name)

Quiz

def life_in_weeks(age):
    weeks_left = (90 - age) * 52
    print(f"You have {weeks_left} weeks left.")

age = int(input("How old are you? "))
life_in_weeks(age)

# Function with more than 1 input,
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# Positional Arguments
greet_with("TK", "Seoul")

# Keyword Arguments
greet_with(location="Seoul", name="TK")

# Input
name = input("What is your name? ")
location = input("Where do you live? ")
greet_with(name, location)
