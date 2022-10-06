def format_name(first_name, last_name):
	""""Return a fill name, neatly formatted"""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = format_name('john', 'lennon')
print(musician)

def full_name_m(first_name, last_name, middle_name=''):
	""""Return a full name, middle name optional"""
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

name1 = full_name_m('aaron', 'jones', 'peter')
name2 = full_name_m('jerry', 'springer')

print(name1)
print(name2)

## can also return a dictionary