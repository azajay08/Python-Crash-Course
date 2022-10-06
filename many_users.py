users = {
	'ajones': {
		'first name': 'aaron',
		'last name': 'jones',
		'location': 'liverpool',
	},

	'mtissari': {
		'first name': 'miro',
		'last name': 'tissari',
		'location': 'malmi',
	},

	'egaliber': {
		'first name': 'elliot',
		'last name': 'galibert',
		'location': 'espoo',
	}
}

for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first name']} {user_info['last name']}"
	location = user_info['location']

	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")