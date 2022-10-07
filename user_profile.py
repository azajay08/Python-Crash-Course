def build_profile(first, last, **user_info):
	""""Build a dictionary with everything we know about user"""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('aaron', 'jones',
							location= 'liverpool',
							field= 'programming')

print(user_profile)