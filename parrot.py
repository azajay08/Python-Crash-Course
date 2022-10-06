message = input("Tell me something, and I will repeat it back to you: ")
print(f"\n{message}\n")


prompt = "\nTell me something and i will repeat it to you: "
prompt += "\nEnter 'quit' and I will quit it. "

message = " "

while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message)