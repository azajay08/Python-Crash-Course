game_consoles = ['xbox 360', 'sega megadrive', 'super nintendo', 'playstation5', 'omega']
print(game_consoles[0].title())

game_consoles = ['xbox 360', 'sega megadrive', 'super nintendo', 'playstation5', 'omega']
print(game_consoles[-1].title())

message1 = f"My first gaming console was the {game_consoles[-1].title()}"
message2 = f"But my current gaming console is the {game_consoles[3].title()}"
print(f'{message1},\n{message2}\n')

# -1 fetches the last of the list 

# Moving parts of the elements

print("\nmoving\n")
print(game_consoles)
game_consoles[0] = "xbox one"
print(game_consoles)
game_consoles.append('xbox 360')
print(game_consoles)
# empty to adding
print("\nadding\n")
game_consoles = []
print(game_consoles)
game_consoles.append('xbox 360')
print(game_consoles)
game_consoles.append('xbox one')
game_consoles.append('playstation5')
print(game_consoles)
# inserting 
print("\ninserting\n")
game_consoles.insert(1, 'omega')
print(game_consoles)
game_consoles.insert(0, 'sega saturn')
print(game_consoles)

# deleting elements
print("\ndeleting\n")
del game_consoles[0]
print(game_consoles)

# pop
print("\npop\n")
print(game_consoles)
popped_gaming_consoles = game_consoles.pop()
print(game_consoles)
print(popped_gaming_consoles)
print(game_consoles)


print(f"The last console I owned was {popped_gaming_consoles.title()}.\n")
game_consoles.append('PS4')
game_consoles.append('playstation5')
print(game_consoles)
# pop certain element
never_owned = game_consoles.pop(2)
print(game_consoles)
print(f"I have never owned the {never_owned.title()}.\n")

# Removing by value

print(game_consoles)
game_consoles.remove('omega')
print(game_consoles)

# Removing by value using variable

game_consoles.insert(1,'xbox one')
game_consoles.insert(3, 'xbox series x')
print(game_consoles)

nahh = 'xbox series x'
game_consoles.remove(nahh)
print(game_consoles)
print(f"\nI won't buy the {nahh.title()}, because I have a {game_consoles[3].title()}\n")






