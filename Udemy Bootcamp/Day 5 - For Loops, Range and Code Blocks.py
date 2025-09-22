Loops
For Loop

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")


total_score = sum(student_scores)

sum = 0
for score in student_scores:
    sum += score
print(sum)
# print(total_score) 도 가능

# max 함수 대신하기
latter = 0
for score in student_scores:
    if latter < score:
        latter = score
    elif latter > score:  #불필요
        latter = latter   #불필요
print(latter)


Range Function

for number in range(1, 10, 3): #두번째 인자, 즉 후속 범위는 불포함. 세번째 인자는 step
  print(number)

total = 0
for number in range(1, 101):
  total += number
print(total)

FizzBuzz
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)



Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

var1 = ''
for letter in letters:
    if len(var1) == nr_letters:
        var1 = var1
    elif len(var1) < nr_letters:
        var1 = var1 + random.choice(letters)

var2 = ''
for symbol in symbols:
    if len(var2) == nr_symbols:
        var2 = var2
    elif len(var2) < nr_symbols:
        var2 = var2 + random.choice(symbols)

var3 = ''
for number in numbers:
    if len(var3) == nr_numbers:
        var3 = var3
    elif len(var3) < nr_numbers:
        var3 = var3 + random.choice(numbers)

password = var1+var2+var3
print(password)

password2 = list(password)
random.shuffle(password2)
final = "".join(password2)
print(final)

print(f"Your password is: {final}") #또는 password 변수
