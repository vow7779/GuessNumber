"""Generate a random number between 1 and upper_bound provided by user (including 1 and upper_bound).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right until he gets it right.
Also display the count to guess the right answer"""

import random


play = True  # To loop continously
while play:
    flag = True  # Flag to check if the entry is digit or not.
    while flag:
        upnum = input("Please enter the upper bound: ")
        if upnum.isdigit():
            up_bound = int(upnum)
            flag = False
        else:
            print("Invalid entry, please try again")

    print(f"Starting game... Guess the number between 1 to {up_bound}")
    computer_guess = random.randint(1, up_bound)
    user_guess = None
    count = 0

    while user_guess != computer_guess:
        user_guess = int(input("Enter your guess:"))
        count += 1
        if user_guess < computer_guess:
            print("Your guess is lower than the computer's")
        elif user_guess > computer_guess:
            print("Your guess is higher than the computer's")
        elif user_guess == computer_guess and count == 1:
            print("Hurray! You guessed it in your first attempt")
        else:
            print(f"You guessed it in {count} attempts")

    again = input("Game over, would you like to play again? (y/n) ").lower()
    if again == "y":
        play = True
        print("restarting...")
    elif again == "n":
        play = False
        print("Thanks for playing, Byee")
    else:
        again = input("Invalid entry, would you like to play again? (y/n) ").lower()
