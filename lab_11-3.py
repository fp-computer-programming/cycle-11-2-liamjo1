# Liam O'Hara
import random

def number_guess():
    # Through the number guess, generate a number between 1 and 100
    secret_number = random.randint(1, 100)
    
    while True:
        # Then ask the user to guess a number
        user_guess = int(input("Guess the number between 1 and 100: "))
        
        # Check if the guessed number is correct
        if user_guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            # Provide a hint whether the number is higher or lower
            if user_guess < secret_number:
                print("Incorrect! Try a higher number.")
            else:
                print("Incorrect! Try a lower number.")

# Example usage:
number_guess()