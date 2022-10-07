def make_pizza(size, *toppings):
	"""can call multiple arguments"""
	print(f'\nMaking a {size}" pizza with the following toppings:')
	for topping in toppings:
		print(f"- {topping}")