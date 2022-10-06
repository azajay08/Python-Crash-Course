pets = ['dog', 'cat', 'turtle', 'cat', 'horse', 'hamster']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
print(pets)


print("\n\n------****------\n")

def describe_pet(animal_type, pet_name):
	""""Displays info about pets"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'lenny')

## really handy, can arrange function whatever way with parameter call
describe_pet(pet_name='lenny', animal_type='hamster')