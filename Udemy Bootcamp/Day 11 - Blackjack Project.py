import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ").lower()

def deal_card():
    return random.choice(cards)

def calculate_score(score):
    total_score = 0
    for num in score:
        total_score += num
        if total_score == 21:
            return 0
        elif total_score > 21:
            score.remove(num)
            score.append(1)
            return total_score
        
user_cards = []
computer_cards = []

for card in cards:
    if len(user_cards) < 2:
        user_cards.append(deal_card())
    if len(computer_cards) < 2:
        computer_cards.append(deal_card())
print(user_cards, computer_cards)

score = user_cards
print(calculate_score(score))
