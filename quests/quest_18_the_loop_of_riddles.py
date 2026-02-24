secret_number = 7
guess = 0 

print ("Welcome to the Guessing Game!")
print ("Try to guess my secret number between 1 and 10.")
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print ("Too low, try again. ")
    elif guess >secret_number:
        print ("Too high, try again. ")
    else:
        print ("Congratulations! It's correct!")
5