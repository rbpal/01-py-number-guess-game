import random

play_again = 'y'

while play_again.lower() == 'y':
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)

    # Get the user's name
    name = input("What is your name: ")
    print(f"Hello {name}!\n")

    # Initialize variables
    try_count = 0
    user_number = None  # Ensure user_number is defined before the loop

    # Start the guessing loop
    while user_number != number:
        try:
            user_number = int(input("Guess the number between 1 and 100: "))
            try_count += 1

            if user_number == number:
                print(f"Congratulations, {name}! You guessed the RIGHT number. This was your {try_count} try.")
            elif user_number < number:
                print(f"Sorry, {name}, you guessed a LOWER number. This was your {try_count} try.")
            else:
                print(f"Sorry, {name}, you guessed a HIGHER number. This was your {try_count} try.")
        except ValueError:
            print("Please enter a valid integer.")

    play_again = input("Do you want to play again? (y/n): ")

print("Thank you for playing!")
