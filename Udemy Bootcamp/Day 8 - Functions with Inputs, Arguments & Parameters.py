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

Love Calculator
# 내 답
true_list = ["t", "r", "u" ,"e"]
love_list = ["l", "o", "v", "e"]

def calculate_love_score(name1, name2):
    true_count = 0
    for char in name1:
        count = true_list.count(char)
        if count == 1:
            true_count += 1
    for char in name2:
        count = true_list.count(char)
        if count == 1:
            true_count += 1
    
    love_count = 0
    for char in name1:
        count = love_list.count(char)
        if count == 1:
            love_count += 1
    for char in name2:
        count = love_list.count(char)
        if count == 1:
            love_count += 1

    print(f"{true_count}{love_count}")

name1 = "Kanye West".lower()
name2 = "Kim Kardashian".lower()
calculate_love_score(name1, name2)

# 실제로 아래처럼 간결하게 가능
def calculate_love_score(name):
    score_true = name.count("t")+name.count("r")+name.count("u")+name.count("e")
    score_love = name.count("l")+name.count("o")+name.count("v")+name.count("e")

    print(f"{score_true}{score_love}")

name1 = "Kanye West".lower()
name2 = "Kim Kardashian".lower()
name = name1+name2
calculate_love_score(name)






