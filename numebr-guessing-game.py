import time
import random

def compare_numbers(a, b):
    if a < b:
        return 0
    return 1

print("Welcome to the Number Guessing Game!")
time.sleep(2)
print("I'm thinking of a number between 1 and 100.")
time.sleep(2)
print("You have 5 chances to guess the correct number.")
end_game = 5
start = 0
time.sleep(2)
print("Please select the difficulty level:")
time.sleep(2)
print("1. Easy (10 chances)")
time.sleep(3)
print("2. Medium (5 chances)")
time.sleep(3)
print("3. Hard (3 chances)")
time.sleep(2)
print("Enter your choice:")
choice = input("> ")

if choice == '1':
    chances = 10
    print("Great! You have selected the Easy difficulty level")
    time.sleep(1)
elif choice == '2':
    chances = 5
    print("Great! You have selected the Medium difficulty level")
    time.sleep(1)
elif choice == '3':
    chances = 3
    print("Great! You have selected the Hard difficulty level")
    time.sleep(1)

print("Let's start the game!")
time.sleep(1)
stop = False

while stop != True and start < end_game :
    i = 0
    computers_guess = random.randint(1, 101)
    win = False
    while i < chances:
        print("Enter your guess: ")
        time.sleep(1)
        guess = input("> ")
        int_guess = int(guess)
        if computers_guess == int_guess:
            print(f"Congratulations! You guessed the correct number in {i+1} attempts")
            win = True
            break
        if compare_numbers(computers_guess, int_guess) == 0:
            print(f"Incorrect! The number is less than {int_guess}.")
        else:
            print(f"Incorrect! The number is greater than {int_guess}.")
        i += 1
        time.sleep(1)

    if win == False:
        print("You failed!")
        time.sleep(1)
        print("Do you want to try again?")
    else:
        print("Up for another round?")
    time.sleep(1)
    response = input("> ")
    if response == "No":
        print("I'm sorry. Maybe next time.")
        stop = True;
    elif response == "Yes":
        print("Great! Let's play again!")
        time.sleep(1)
        print("How difficult do you want this round to be?")
        time.sleep(1)
        print("Enter your choice: ")
        another_choice = input("> ")
        if another_choice == "1":
            print("Great! You have selected the Easy difficulty level")
            chances = 10
            time.sleep(1)
        elif another_choice== "2":
            print("Great! You have selected the Medium difficulty level")
            chances = 5
            time.sleep(1)
        else:
            print("Great! You have selected the Hard difficulty level")
            chances = 3
            time.sleep(1)
        start += 1













