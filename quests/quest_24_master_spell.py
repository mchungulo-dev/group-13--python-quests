def ask_for_age():
    age = input("Enter your age: ")
    return age

def can_they_vote(age):
    age = int(age)
    if age >= 18:
        print("You can vote")
    else:
        print("You cant vote.")

age = ask_for_age()
can_they_vote(age)