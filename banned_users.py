banned_users = ['jerry', 'karen', 'lotta', 'miro']
user = 'david'
if user not in banned_users:
	print(f"{user.title()}, you can now comment")
else:
	print(f"{user.title()}, You are banned from commenting")
user = 'jerry'
if user not in banned_users:
	print(f"{user.title()}, you can now comment")
else:
	print(f"{user.title()}, You are banned from commenting")