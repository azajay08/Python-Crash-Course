answer = 1
if answer != 42:
	print("Sorry this is the incorrect answer, Please try again")

# same as C <= => == !=
# && and || different, uses 'and' & 'or'

age = 23
age1 = 30
if age <= 25 and age >= 20:
	print("true")
else:
	print("fasle")

if age1 <= 25 and age1 >= 20:
	print("true")
else:
	print("false")

if age <= 25 or age1 <= 20:
	print("true")
else:
	print("false")