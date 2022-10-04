print("\nSqaure\n")
squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)
print(squares)
# more concise - 11 is the range in which it prints the list
squares = []
for value in range(1, 11):
	squares.append(value ** 2)
print(squares)

# even more concise
squares = [value ** 2 for value in range(1, 11)]
print(squares)