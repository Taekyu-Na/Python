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








