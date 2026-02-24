# quest_27_the_fizzbuzz_test.py

# Loop through numbers 1 to 100
for i in range(1, 101):
    # Check if number is divisible by both 3 and 5 first
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Check if divisible by 3
    elif i % 3 == 0:
        print("Fizz")
    # Check if divisible by 5
    elif i % 5 == 0:
        print("Buzz")
    # If none of the above, just print the number
    else:
        print(i)