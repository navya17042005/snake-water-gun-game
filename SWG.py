import random

# 1 for snake, -1 for water, 0 for gun
computer = random.choice([-1, 1, 0])

# Get user input
youstr = input("Enter your choice (s for snake, w for water, g for gun): ").strip().lower()

# Dictionaries to map choices
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

# Get the corresponding value for the user's input
you = youDict.get(youstr)

# Check if the user's input is valid
if you is None:
    print("Invalid choice! Please choose 's', 'w', or 'g'.")
else:
    # Display choices
    print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

    # Check the outcome
    if computer == you:
        print("It's a draw!")
    elif (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
        print("You win!")
    else:
        print("You lose!")
