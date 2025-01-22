import random

def guess_the_number():
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    
    # Generate a random number between lower_bound and upper_bound
    number_to_guess = random.randint(lower_bound, upper_bound)
    
    print("Welcome to 'Guess the Number'!")
    print(f"Guess a number between {lower_bound} and {upper_bound}.")
    
    attempts = 0
    while True:
        # Take the user's guess
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        # Check if the guess is correct
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

# Call the function to start the game
guess_the_number()
