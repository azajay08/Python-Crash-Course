dimensions = (20, 50)
print(dimensions[0])
print(dimensions[1])

# cannot change the value of a Tuple,
# Tuple uses ( ) instead of [ ]. Also
# the comma needs to be there in order for it to be 
# initialised as a Tuple even for just one

for dimension in dimensions:
	print(dimension)

# re defining a Tuple

print("\nOriginal Tuple")
for dimension in dimensions:
	print(dimension)
dimensions = (30, 60)
print("\nNew Tuple")
for dimension in dimensions:
	print(dimension)
