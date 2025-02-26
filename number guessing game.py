import random

number = random.randint(1, 100)
attempts = 0

while True:

    try:
        guess = int(input("Enter a number between 1 and 100: "))
        if not (1 <= guess <= 100):
            print("Number you entered was out of range, it must be between 1 and 100.")
            continue
        if guess < number:
            print("too low")
            attempts += 1
            continue
        elif guess > number:
            print("too high")
            attempts += 1
            continue
        else:
            attempts += 1
            print(f"You guessed the number correctly after {attempts} attempts.")
            print(f"The number was {number}.")
        
        quit_continue = input("Press any key to continue or 'q' to quit the game... ").lower()

        if quit_continue == 'q':
            break
        else:
            print("Starting a new game...")
            number = random.randint(1, 100)
            attempts = 0
            continue
        
    except ValueError:
        print("Invalid input")
