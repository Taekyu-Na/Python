Functions

def my_function():
    print("Hello")
    print("Bye")

my_function()

Reeborg's World

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Draw Square
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

#World Hurdles Challenge
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for number in range(1, 7):
    jump()
여기서 for number in range(6):
    jump() 도 가능

Code Blocks / Indentation

def my_function():
    if sky == "clear":
        print("blue")
    elif sky == "cloudy":
        print("grey")
    print("Hello")
print("World")

While Loop
# while something_is_true
    # Do something repeatedly

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)

#World Hurdles Challenge 2
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True:
    jump()

while not at_goal():
    jump()

#World Hurdles Challenge 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

#World Hurdles Challenge 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
            
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

Project
15일차 강의 끝나고 와서 Infinite Loop 해결해보기

def turn_right():
    turn_left()
    turn_left()
    turn_left()
             
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()





