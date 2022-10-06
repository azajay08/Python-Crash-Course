name = input("Please enter your name: ")
print(f"Hello, {name}!")

print("\n---***---\n")

prompt = "If you say your name, we can personlise the messages you see."
prompt += "\nWhat is your name? "

name = input(prompt)
print(f"\nHello, {name}!\n")

age = input("How old are you? ")
age = int(age)
if age >= 30:
	print("\nOooof, getting old!")
else:
	print("\nAhh, still a spring chicken")