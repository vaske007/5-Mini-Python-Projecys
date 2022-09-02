# We are going to keep track of how many times the user wins, and how many times the computer wins.
import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"] # By using the [] we are making a list. Lists are a type of data structure and they are collections of elements. We have multiple elements, a.k.a strings.
#  index     0        1          2   ...
# We can access these elements individually by using something known as an index. For example options[0] will output "rock".

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    # Here we are checking if the users input is not a string in the list.
    if user_input not in options :
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2



print("Goodbye")