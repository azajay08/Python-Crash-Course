requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies!")

requested_toppings = ['mushrooms', 'cheese', 'bacon', 'pepperoni']
if 'cheese' in requested_toppings:
	print('true')
else:
	print('false')

if 'chicken' in requested_toppings:
	print('true')
else:
	print('false')

if 'mushrooms' in requested_toppings:
	print("adding mushrooms")
if 'chicken' in requested_toppings:
	print("adding chicken")
if 'bacon' in requested_toppings:
	print("adding bacon")
print("\n-----\n")

# more for play

requested_toppings = ['mushrooms', 'cheese', 'bacon', 'pepperoni']
if requested_toppings:
	for requested_topping in requested_toppings:
		if requested_topping == 'bacon':
			print(f"We are sorry but we have ran out of {requested_topping}\n")
		else:
			print(f"adding {requested_topping}.\n")
	print("finished making your pizza.")
else:
	print("Are you sure you want a plain pizza?")

print("\n-----\n")

requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		if requested_topping == 'bacon':
			print(f"We are sorry but we have ran out of {requested_topping}\n")
		else:
			print(f"adding {requested_topping}.\n")
	print("finished making your pizza.")
else:
	print("Are you sure you want a plain pizza?")

print("\n-----\n")
requested_toppings = ['mushrooms', 'blue cheese', 'bacon', 'pepperoni',
						'cheese']
available_toppings = ['mushrooms', 'peppers', 'bacon', 'pineapple', 
						'chicken', 'cheese', 'garlic']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"adding {requested_topping}\n")
	else:
		print(f"Unfortunately we do that have {requested_topping} in stock\n")
print("Finished making your pizza!")
	