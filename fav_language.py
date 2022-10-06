fav_language = '|python|         '
new_language = '|java|'
print(fav_language, new_language)

fav_language = '|python|         '
new_language = '|java|'
print(fav_language.rstrip(), new_language)

fav_language = '|python|'
new_language = '         |java|'
print(fav_language, new_language)

fav_language = '|python|'
new_language = '         |java|'
print(fav_language, new_language.lstrip())

fav_language = '|python|'
new_language = '         |java|         '
lan_language = '|ruby|'
print(fav_language, new_language, lan_language)

fav_language = '|python|'
new_language = '         |java|         '
lan_language = '|ruby|'
print(fav_language, new_language.strip(), lan_language)

# dictionary

fav_languages = {
	'aaron': 'python',
	'elliot': 'ruby',
	'miro': 'c',
	'lotta': 'ruby',
	'david': 'java',
	}

language = fav_languages['lotta'].title()
print(f"\n\nLotta's favourite language is {language}.\n\n\n")


#########

for name, language in fav_languages.items():
	print(f"\n{name.title()}'s favourite language is {language.title()}.")

print('\n\n')
for name in fav_languages.keys():
	print(name.title())
print("\n\n----****----\n\n")

#### 

fav_lang = {
	'jen': ['python', 'ruby', 'c#'],
	'kayla': ['c', 'haskell'],
	'adam': ['c', 'swift', 'python'],
	'elliot': ['html'],
}
for name, languages in fav_lang.items():
	print(f"\n{name.title()}'s favourite languages are:")
	for language in languages:
		if language == 'html' or language == 'c':
			language = f"{language.upper()}"
			print(f"\t{language}")
		else:
			print(f"\t{language.title()}")

