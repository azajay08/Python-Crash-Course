confirmed_users = []
unconfirmed_users = ['aaron', 'alex', 'edward']

while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print(f"Verifying user: {current_user.title()}")
	confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())