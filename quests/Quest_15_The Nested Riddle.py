direction = input("Do you want to go left or right? ")
if direction == "left":
    action = input("Do you 'swim' or 'wait'? ")
    if action == "swim":
        print("You find a treasure!")
    else:
        print("Nothing happens while you wait.")
else:
        print("You went right and found a dead end.")