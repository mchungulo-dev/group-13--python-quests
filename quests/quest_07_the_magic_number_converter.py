# Ask the user for their birth year, convert it to an integer, and calculate their approximate age.
birth_year = input("What is your birth year?")
age_int = int(birth_year)
current_year = 2026
user_age = current_year - age_int
print(f"Your approximate age is: {user_age}")