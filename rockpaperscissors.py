# Creating a rock paper scissors game in python

import random
import time


def countdown(t=3):
  while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer)
    # Use the time.sleep() function to delay the execution
    time.sleep(1)
    t -= 1
  print("Shoot!")

# Call the countdown function
countdown()

while True:
# Define the list of choices
  choices = ['rock', 'paper', 'scissors']

# Get the player's choice
  computer = random.choice(choices)

# Get the player's choice
  player = None

# Loop until the player enters a valid choice
  while player not in choices:
    player = input("Rock, Paper, or Scissors?: ").lower()
    if player not in choices:
      print("Please try again.")

# Compare the player's choice with the computer's choice
  if player == computer:
    print("Computer: ", computer)
    print("Player: ", player)
    print('Tie!')
  elif player == "paper":
    if computer == "rock":
      print("Computer: ", computer)
      print("Player: ", player)
      print("You win!")
    else:
      print("Computer : ", computer)
      print("Player: ", player)
      print("You lose!")
  elif player == "rock":
    if computer == "scissors":
      print("Computer: ", computer)
      print("Player: ", player)
      print("You win!")
    else:
      print("Computer: ", computer)
      print("Player: ", player)
      print("You lose!")
  elif player == "scissors":
    if computer == "paper":
      print("Computer: ", computer)
      print("Player: ", player)
      print("You win!")
    else:
      print("Computer: ", computer)
      print("player: ", player)
      print("You lose!.")
  else:
    print("Try Again")

  play_again = (input('Would you like to play again? Yes/No: ')).lower()

  if play_again != 'yes':
    break

print("Bye!")
