#PenguinyOffical 2026
#67
import random
import time

print(
    r"""
     \      \  __ __  _____\_ |__   ___________   /  _____/_____    _____   ____  
     /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___\__  \  /     \_/ __ \ 
    /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \/ __ \|  Y Y  \  ___/ 
    \____|__  /____/|__|_|  /___  /\___  >__|     \______  (____  /__|_|  /\___  >
            \/            \/    \/    \/                \/     \/      \/    \/ 
"""
)

# Track whether levels are unlocked across multiple game rounds
unlocked_level_67 = True
unlocked_level_99 = False  # Set to True for testing

while True:
    # Step 1: Select difficulty level
    max_number = 0
    current_level = 0  # Track which level is being played this round

    while True:
        try:
            prompt = "Choose a level from 1-5"
            if unlocked_level_67:
                prompt += " (or 67 for Elite Mode)"
            if unlocked_level_99:
                prompt += " (or 99 for ??? Mode)"
            prompt += " [0 to quit]: "

            level = int(input(prompt))

            if level == 0:
                print("Thanks for playing!")
                exit()
            elif level == 1:
                max_number = 10
                current_level = 1
                break
            elif level == 2:
                max_number = 50
                current_level = 2
                break
            elif level == 3:
                max_number = 100
                current_level = 3
                break
            elif level == 4:
                max_number = 500
                current_level = 4
                break
            elif level == 5:
                max_number = 1000
                current_level = 5
                break
            elif level == 67:
                if unlocked_level_67:
                    print("🔥 Elite mode activated! The max number is now 10,000!\n")
                    max_number = 10000
                    current_level = 67
                    break
                else:
                    print("🔒 Level 67 is locked! Beat Level 5 first to unlock it.\n")
            elif level == 99:
                if unlocked_level_99:
                    print("❓ ??? Mode activated! The maximum range is completely unknown!\n")
                    max_number = random.randint(500, 10000)
                    current_level = 99
                    break
                else:
                    print("🔒 Level 99 is locked!\n")
            else:
                print("Please pick a valid level number.\n")
        except ValueError:
            print("Please enter a valid integer.\n")

    # Step 2: Generate the target number
    number = random.randint(1, max_number)
    start_time = time.time()

    # Step 3: Game loop
    while True:
        try:
            # Mask the max number if in Level 99
            display_max = "???" if current_level == 99 else max_number
            guess = int(input(f"Guess the number (1-{display_max})!: "))

            if guess == number:
                end_time = time.time()
                total_time = round(end_time - start_time, 2)
                print(f"Speedrun Time: {total_time} seconds!")
                print(f"You Win!  {number}!")

                # Unlock Level 67 if player beats Level 5
                if current_level == 5 and not unlocked_level_67:
                    unlocked_level_67 = True
                    print("UNLOCKED! You beat Level 5 and unlocked Level 67 (Elite Mode)!")

                if current_level == 67:
                    unlocked_level_99 = True
                    print("You unlocked a new level!")
                print("\n" + "=" * 40 + "\n")
                break
            elif guess > number:
                print("Too High!")
            else:
                print("Too Low!")
        except ValueError:
            print("Invalid input! Please enter a number.")
