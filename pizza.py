pizza = {
	'crust': 'thick',
	'toppings': ['extra cheese', 'mushrooms', 'pepperoni'],
}

print(f"You ordered a {pizza['crust']}-crust pizza "
"with the following toppings")

for topping in pizza['toppings']:
	print(f"\t{topping}")
	