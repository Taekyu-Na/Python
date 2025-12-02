Randomization

import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.my_favorite_no)

random_int_0to1notincluded = random.random()
print(random_int_0to1)

random_float = random.uniform(3, 4)
print(random_float)

random_head_tail = random.randint(0,1)

if random_head_tail == 0:
    print("Heads")
else:
    print("Tails")

Python List
var = [item1, item2]

states_of_us = ["Texas", "New York", "New Jersey"]
print(states_of_us[0]) #순서에 따라 출력되며, [0]을 통해 n번째 출력 가능. 음의 인덱스도 사용가능
states_of_us[0] = "Tesas" # 변환도 가능
states_of_us.append("TKland") # 단일값 추가도 가능
states_of_us.extend(["TK", "Test"]) # 다중값 추가도 가능
print(states_of_us)

import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))

random_index = random.randint(0, 4) #도 가능

Index Error - 리스트 초과시 발생

Nested List - 중첩 리스트
element = ["Water", "Fire", "Soil"]
chemical = ["H2O", "Sodium"]

combined = [element, chemical]
print(combined)

Project

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if my_choice <= 2 and my_choice >= 0:
    print(game_image[my_choice])

computer_choice = (0, 1, 2)
computer_choice = random.choice(computer_choice)
print("Computer chose:")
print(game_image[computer_choice])

if my_choice >= 3 or my_choice < 0:
    print("Please input correct number")

elif my_choice == computer_choice:
    print("It's a draw")

elif my_choice == 0 and computer_choice == 2:
    print("You win!")

elif my_choice == 2 and computer_choice == 0:
    print("You lose")

elif my_choice < computer_choice:
    print("You lose")

elif my_choice > computer_choice:
    print("You win!")






