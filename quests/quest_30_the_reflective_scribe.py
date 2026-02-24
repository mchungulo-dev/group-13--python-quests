# quest_30_the_reflective_scribe.py

# I am reflecting on Quest 27 (FizzBuzz)
# I used a 'for' loop to go through numbers 1 to 100.
for i in range(1, 101):
    # This 'if' checks if the number is divisible by 3 AND 5.
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # This 'elif' checks for just multiples of 3.
    elif i % 3 == 0:
        print("Fizz")
    # This 'elif' checks for just multiples of 5.
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)