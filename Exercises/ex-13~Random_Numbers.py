import random
import os
os.system('cls' if os.name == 'nt' else 'clear')

# low = 1
# high = 100
# options = ("rock", "paper", "scissors")
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# number = random.randint(low, high)
# number = random.random()
# option = random.choice(options)
# random.shuffle(cards)

#print(cards)

# Number guessing game!
# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True

# print("Python Number Guessing Game")
# print(f"Select a number between {lowest_num} and {highest_num}")

# while is_running:
#     try:
#         guess = int(input("Enter your guess (0 to quit): "))
#         if guess == 0:
#             print("Goodbye!")
#             break
#         guesses += 1
#         if guess < lowest_num or guess > highest_num:
#             print(f"Chosen number is out of range!")
#         elif guess < answer:
#             print("Too low! Try again")
#         elif guess > answer:
#             print("Too high! try again!")
#         else:
#             print(f"Correct! The answer was {answer}")
#             print(f"Number of guesses it took: {guesses}")
#             is_running = False

#     except ValueError:
#         print("Invalid Number")
    

# Rock paper scissors game!

options  = ("rock", "paper", "scissors")
computer = random.choice(options)
player = ''
while player not in options: 
    player  = input("Enter a choice (rock, paper or scissors): ").lower()

print(f"Player: {player}")
print(f"Computer: {computer}")

if player == computer:
    print("It's a tie!")
elif player == "rock" and computer == "scissors":
    print("You Win!")
elif player == "paper" and computer == "rock":
    print("You Win!")
elif player == "scissors" and computer == "paper":
    print("You Win!")
else:
    print("You Lose....")

    
    
