# PenguinyOffical 2026
# The Number Game V1
# All code in this program is not copyrights lol idc.

import random
import time

print(r"""
     \      \  __ __  _____\_ |__   ___________   /  _____/_____    _____   ____  
     /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___\__  \  /     \_/ __ \ 
    /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \/ __ \|  Y Y  \  ___/ 
    \____|__  /____/|__|_|  /___  /\___  >__|     \______  (____  /__|_|  /\___  >
        \/            \/    \/     \/                \/     \/      \/     \/ 
""")
# Step 1: Select difficulty level
max_number = 0
while True:
    level = int(input("Choose a level from 1-5: "))

    if level == 1:
        max_number = 10
        break
    elif level == 2:
        max_number = 50
        break
    elif level == 3:
        max_number = 100
        break
    elif level == 4:
        max_number = 500
        break
    elif level == 5:
        max_number = 1000
        break
    else:
        print("Please pick a number from 1 to 5.\n")

# Step 2: Generate the target number
number = random.randint(1, max_number)
start_time = time.time()

# Step 3: Repeatedly prompt until correct
while True:
    guess = int(input(f"Guess the number (1-{max_number})!: "))

    if guess == number:
        end_time = time.time()
        total_time = round(end_time - start_time, 2)
        print(f"⏱️ Speedrun Time: {total_time} seconds!")
        print("You Win!")
        break
    elif guess > number:
        print("Too High!")
    else:
        print("Too Low!")
