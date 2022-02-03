from os import system
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def deal_card():
  """returns a random card from the deck"""
  random_card = random.choice(cards)
  return random_card

def compare(player_score, computer_score):
  if player_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if player_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif player_score == 0:
    return "Win with a Blackjack 😎"
  elif player_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif player_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤" 

def play_game():
  player_cards = []
  pc_cards = []
  is_game_over = False

  print(logo)
  for _ in range(2):
    player_cards.append(deal_card())
    pc_cards.append(deal_card())

  while not is_game_over:
    player_score = calculate_score(player_cards)
    pc_score = calculate_score(pc_cards)

    print(f"Your cards {player_cards} and your score is {player_score}")
    print(f"Computer's first card is {pc_cards[0]}")

    if player_score == 21 or pc_score == 21 or player_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == 'y':
        player_cards.append(deal_card())
      else:
        is_game_over = True

  while pc_score != 0 and pc_score < 17:
    pc_cards.append(deal_card())
    pc_score = calculate_score(pc_cards)

  print(f"Your final hand: {player_cards}, final score: {player_score}")
  print(f"Computer's final hand: {pc_cards}, final score: {pc_score}")
  print(compare(player_score, pc_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  system("clear")
  play_game()
