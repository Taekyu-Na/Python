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

