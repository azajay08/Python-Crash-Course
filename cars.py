cars = ['bmw', 'vw', 'toyota', 'mercedes', 'tesla']
for car in cars:
	if car == 'vw':
		print(car.upper())
	elif car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

car = 'Audi'
if car == 'audi':
	print(1)
elif car.lower() == 'audi':
	print(2)