pizza = {
	'crust': 'thick',
	'toppings': ['extra cheese', 'mushrooms', 'pepperoni'],
}

print(f"You ordered a {pizza['crust']}-crust pizza "
"with the following toppings")

for topping in pizza['toppings']:
	print(f"\t{topping}")

# multi arguments using asterisk *
def make_pizza(size, *toppings):
	"""can call multiple arguments"""
	print(f'\nMaking a {size}" pizza with the following toppings:')
	for topping in toppings:
		print(f"- {topping}")

make_pizza(12, 'cheese', 'tomato')

make_pizza(16, 'olives', 'cheese', 'pepperoni')
	