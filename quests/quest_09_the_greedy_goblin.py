# Goblin = 27 gold pieces to share among 4 friends. Calculate how many pieces each friend gets & how many the goblin keeps.
goblin_pieces = 27
goblin_friends = 4
friends_get = goblin_pieces // goblin_friends
goblin_remainder = goblin_pieces % goblin_friends
print(f"The Goblin's friends will each get {friends_get} gold pieces, leaving the Goblin with {goblin_remainder} gold pieces.")
