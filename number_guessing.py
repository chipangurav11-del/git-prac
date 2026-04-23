import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("=== NUMBER GUESSING GAME ===")
    print("I have chosen a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low.")
            elif guess > secret_number:
                print("Too high.")
            else:
                print("Correct! You guessed the number.")
                print("Number of attempts:", attempts)
                break

        except ValueError:
            print("Please enter a valid number.")

number_guessing_game()