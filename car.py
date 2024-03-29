class Car:
	"""A simple class to represent a car"""

	def __init__(self, make, model, year):
		"""Initialize make model and year"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name"""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showingthe car's mileage"""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""
		Set the odometer to given value
		reject if attempted to roll back
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back the meter.")

	def increment_odometer(self, miles):
		"""Add given amount to mileage"""
		self.odometer_reading += miles


my_new_car = Car('tesla', 'model x', '2022')
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 2306
my_new_car.read_odometer()

my_new_car.update_odometer(12377)
my_new_car.read_odometer()

my_new_car.increment_odometer(523)
my_new_car.read_odometer()