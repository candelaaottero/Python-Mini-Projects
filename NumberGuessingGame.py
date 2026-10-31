import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
print("Please select the difficulty level:\n\t1. Easy (10 chances)\n\t2. Medium (5 chances)\n\t3. Hard (3 chances)")

difficulty_level = int(input("Enter your choice: "))
chances = 0

if (difficulty_level == 1):
    print("Great! You have selected the Easy difficulty level. Let's start the game!")
    chances = 10
elif (difficulty_level == 2):
    print("Great! You have selected the Medium difficulty level. Let's start the game!")
    chances = 5
elif (difficulty_level == 3):
    print("Great! You have selected the Hard difficulty level. Let's start the game!")
    chances = 3
else:
    print("Incorrect number.")

number = random.randint(1,100)

for i in range(chances):
    guess = int(input("Enter your guess: "))
    if (guess == number):
        print(f"Congratulations! You guessed the correct number in {i} attempts.")
        break
    else:
        if (number < guess):
            print(f"Incorrect! The number is less than {guess}.")
        else:
            print(f"Incorrect! The number is greater than {guess}.")