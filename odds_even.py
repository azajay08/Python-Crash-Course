number = input("Enter a number to see if it is odd or even: ")
number = int(number)

if number % 2 == 0:
	print(f"\nThe number {number} is even.")
else:
	print(f"\nThe number {number} is odd.")