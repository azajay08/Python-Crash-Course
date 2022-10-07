class Car:
	"""A simple class to represent a car"""

	def __init__(self, make, model, year):
		"""Initialize make model and year"""
		self.make = make
		self.model = model
		self.year = year

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name"""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

my_new_car = Car('tesla', 'model x', '2022')
print(my_new_car.get_descriptive_name())