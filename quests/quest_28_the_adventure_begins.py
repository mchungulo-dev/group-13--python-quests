# quest_28_the_adventure_begins.py

def start_game():
    print("--- The Crystal Cave ---")
    print("You stand at a crossroads. Do you go 'left' towards the light or 'right' into the dark?")
    choice = input("> ").lower()

    if choice == "left":
        forest_path()
    elif choice == "right":
        dragon_lair()
    else:
        print("You stayed still for too long and turned into a statue. Game Over.")

def forest_path():
    print("\nYou found a beautiful forest and a hidden treasure chest!")
    print("You win! (Ending 1)")

def dragon_lair():
    print("\nYou walked straight into a sleeping dragon's lair.")
    print("Do you 'hide' or 'run'?")
    action = input("> ").lower()
    
    if action == "run":
        print("\nYou escaped safely back to the start.")
        start_game()
    else:
        print("\nThe dragon woke up. Not a good day for you. (Ending 2)")

# Start the adventure
start_game()