# generate random integer values
from random import seed
from random import randint
import random
import time

print("Rock, Paper, or Scissors on 3. Ready?")
input("Press Enter to continue...")
print("1...", end = ' ')
time.sleep(1)
print("2...", end = ' ')
time.sleep(1)
print("3!")
txt = input("Please Type Rock, Paper, or Scissors: ")

# Note that in version 3, the print() function
# requires the use of parenthesis.
print("Your choice: ", txt)

# seed random number generator
random.seed()
# generate some integers
for _ in range(1):
	value = randint(1, 3)


if value == 1:
    # indented four spaces
    print("My choice: Rock")

if value == 2:
    # indented four spaces
    print("My choice: Paper")

if value == 3:
    # indented four spaces
    print("My choice: Scissors")

# decider of who wins
if txt == "Rock" and value == 1:
    print("It's a tie!")

if txt == "Rock" and value == 2:
    print("Paper covers Rock! I win!")

if txt == "Rock" and value == 3:
    print("Rock crushes Scissors! You win!")

if txt == "Paper" and value == 1:
    print("Paper covers Rock! You win!")

if txt == "Paper" and value == 2:
    print("It's a tie!")

if txt == "Paper" and value == 3:
    print("Scissors cut Paper! I win!")

if txt == "Scissors" and value == 1:
    print("Rock crushes Scissors! I win!")

if txt == "Scissors" and value == 2:
    print("Scissors cut Paper! You win!")

if txt == "Scissors" and value == 2:
    print("It's a tie!")