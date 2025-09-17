Conditional, if / else

if condition:
  do this
else:
  do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

Codeblock
if height > 120:                                 #Codeblock1
    print("You can ride the rollercoaster.")     #Codeblock1
else:                                              #Codeblock2
    print("You cannot ride the rollercoaster.")    #Codeblock2

Comparison Operation
>, <, >=, <=, ==, !=
# "=" 1개는 변수 할당
# "==" 2개는 값 일치 확인

Modulo Operator % (나머지 계산)

var1 = int(input("Input any number and you will get either Odd or Even "))

if var1 % 2 == 0:
    print("Even")
else:
    print("Odd")
    
Nested if / else 중첩

if condition:
  if another condition:
    do this
else:
  do this
  
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 18:
        print("You have to pay $7.")
    else:
        print("You have to pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")

Elif
if condition1:
  do A
elif condition2:
  do B
else:
  do C

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")

Multiple IF
if condition1:
  do A
if condition2:
  do B
if condition3:
  do C

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    var2 = input("Do you want a photo take? Type Y for Yes and N for No. ")
    if var2 == "Y":
        bill += 3

    print(f"Your total bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")



print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
else:
    bill += 25
    if pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")

아니면 아래도 가능
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill += 25
else:
  print("You typed the wrong inputs.")

if pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1
print(f"Your final bill is: ${bill}.")

Logical Operators AND OR NOT
#    if age < 12:
#        bill = 5
#        print("Child tickets are $5.")
#    elif age <= 18:
#        bill = 7
#        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55: "45 <= age <= 55 도 가능"
        print("Your ride is free")
#    else:
#        bill = 12
#        print("Adult tickets are $12.")


Project
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
var1 = input('You\'re at a cross road. Where do you want to go?\nType "left" or "right"\n')

if var1.lower() == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    var2 = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if var2.lower() == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        var3 = input("One red, one yellow and one blue. Which colour do you choose?\n")
        if var3.lower() == "red":
            print("It's a room full of fire. Game Over.")
        elif var3.lower() == "blue":
            print("You enter a room of beasts. Game Over")
        else:
            print("You found the treasure! You Win!")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")

# 아래도 가능
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
var1 = input('You\'re at a cross road. Where do you want to go?\nType "left" or "right"\n').lower()

if var1 == "left":
    var2 = input('You\'ve come to a lake. There is an island in the middle of the lake."\n'
                 'Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if var2 == "wait":
        var3 = input('You arrive at the island unharmed. There is a house with 3 doors.\n'
                     'One red, one yellow and one blue. Which colour do you choose?\n').lower()
        if var3 == "red":
            print("It's a room full of fire. Game Over.")
        elif var3 == "blue":
            print("You enter a room of beasts. Game Over")
        elif var3 == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")








