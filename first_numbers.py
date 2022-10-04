import numbers


number = 140_001_001_001
x, y, z = 2, 13, 42
CONST_NUMBERS = 500
print(number)
print(y)
print(z)
print(x, y, z)
print(x / y)
print(CONST_NUMBERS)
CONST_NUMBERS = 4
print(CONST_NUMBERS)


# divisions always revert to floats in python regardles 
# if it is a whole number and even if it is an integer

# multiple variables in one line

# No data type for constant in python but CAPITALISE to 
# treat it as a constant

# range function prints to one less that high end range. 5 is 4
print("\nRange\n")
for value in range(1, 5):
	print(value)

# number list
print("\nNumber List\n")
numbers = list(range(1, 6))
print(numbers)

print("\nEven numbers\n")
even_numbers = list(range(2, 11, 2))
print(even_numbers)


digits = [1, 2, 4, 3, 6, 5, 9, 8, 7, 0]
print(max(digits))
print(min(digits))
print(sum(digits))

