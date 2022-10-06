def get_form_name(first_name, last_name):
	""""return full name"""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

while True:
	print("\nPlease tell me your name: ")
	print("(enter 'q' at any time to exit)")
	fname = input("First name: ")
	if fname == 'q':
		break
	lname = input("Last name: ")
	if lname == 'q':
		break

	form_name = get_form_name(fname, lname)
	print(f"\nHello, {form_name}!")