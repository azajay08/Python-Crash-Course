pizza = {
	'crust': 'thick',
	'toppings': ['extra cheese', 'mushrooms', 'pepperoni'],
}

print(f"You ordered a {pizza['crust']}-crust pizza "
"with the following toppings")

for topping in pizza['toppings']:
	print(f"\t{topping}")

# multi arguments using asterisk *
def make_pizza(*toppings):
	"""can call multiple arguments"""
	print("\nMaking pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")

make_pizza('cheese', 'tomato')

make_pizza('olives', 'cheese', 'pepperoni')
	