# quest_29_the_code_breaker.py
secret_code = "42"

print("--- The Code Breaker ---")

for attempt in range(1, 4):
    guess = input(f"Attempt {attempt}/3 - Enter the code: ")
    
    if guess == secret_code:
        print("Access Granted! You broke the code.")
        break
    else:
        print("Wrong code.")
    
    if attempt == 3:
        print("Out of attempts. System locked.")