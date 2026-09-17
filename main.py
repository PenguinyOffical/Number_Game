#PenguinyOffical
import time
import random
from list import levels
from information import information
user = -1
guesses = 0
max_guesses = 5
print("2026.10.15 First Beta")
print(
    r"""
     \      \  __ __  _____\_ |__   ___________   /  _____/_____    _____   ____  
     /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___\__  \  /     \_/ __ \ 
    /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \/ __ \|  Y Y  \  ___/ 
    \____|__  /____/|__|_|  /___  /\___  >__|     \______  (____  /__|_|  /\___  >
            \/            \/    \/    \/                \/     \/      \/    \/ 
"""
)
level_choice = int(input("Choose a level 1-5: "))

# Dynamic level setup based on user input
level_key = f"level{level_choice}"
max_number = levels[level_key]
answer = random.randint(0, max_number)

# Start the timer RIGHT BEFORE the game loop begins
start_time = time.time()

# Main game loop for ALL levels
while user != answer:
    if level_choice >= 4 and guesses >= max_guesses:
        print(f"You ran out of guesses! The answer was {answer}.")
        break

    if level_choice >= 4:
        user = int(input(f"Guess the number 0-{max_number} (Guesses used: {guesses}/{max_guesses}): "))
    if level_choice == 67:
        information()

    else:
        user = int(input(f"Guess the number 0-{max_number}: "))
        # print(answer) # You might want to remove this cheat for the actual game!

    guesses += 1

# Win message
if user == answer:
    print("You guessed the answer! You win!")
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    print(f'Your time was {total_time} seconds.')
    print("Thanks for playing the beta!")