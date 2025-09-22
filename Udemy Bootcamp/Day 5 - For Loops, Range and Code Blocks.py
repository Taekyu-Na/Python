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

