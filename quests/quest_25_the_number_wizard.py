# quest_25_the_number_wizard.py
secret_number = 42

print("--- Welcome to the Number Wizard ---")

while True:
    guess_input = input("Guess the secret number: ")
    
    if guess_input.isdigit():
        guess = int(guess_input)
        
        if guess == secret_number:
            print("Correct! You found the secret.")
            break 
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
    else:
        print("Please enter a valid whole number.")