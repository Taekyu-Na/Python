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

Caesar Cipher 1

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

def encrypt(original_text, shift_amount):
    encoded_text = ''
# 내 답변
    # for char in original_text:
    #     index = alphabet.index(char)
    #     encoded_text += alphabet[index + shift_amount]
# 선생님 답변
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        encoded_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {encoded_text}")

encrypt(text, shift)

Caesar Cipher 2

#내 답
def caesar(direction, text, shift):
    if direction == "encode":
        cipher_text = ""
        for letter in text:
            shifted_position = alphabet.index(letter) + shift
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        print(f"Here is the encoded result: {cipher_text}")

    elif direction == "decode":
        decrypted_text = ""
        for letter in text:
            shifted_position = alphabet.index(letter) - shift
            shifted_position %= len(alphabet)
            decrypted_text += alphabet[shifted_position]
        print(f"Here is the decoded result: {decrypted_text}")

caesar(direction, text, shift)

# 선생님 답
def caesar(encode_or_decode, original_text, shift_amount):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)

Caesar Cipher 3

# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        elif letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# TODO-3: Can you figure out a way to restart the cipher program?
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        print("Good bye.")
        should_continue = False













