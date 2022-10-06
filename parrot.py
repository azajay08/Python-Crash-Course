message = input("Tell me something, and I will repeat it back to you: ")
print(f"\n{message}\n")


prompt = "\nTell me something and i will repeat it to you: "
prompt += "\nEnter 'quit' and I will quit it. "

message = " "

active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print(message)


# True and False are flags

# can use break like C

# continue will just continue the loop