alien_0 = {'colour': 'green', 'points': 5}
alien_1 = {'colour': 'yellow', 'points': 10}
alien_2 = {'colour': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)


aliens = []

for alien_number in range(30):
	new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# using the slice to just print out 5 instead of 30

# now to change the first 3's characteristics

for alien in aliens[:3]:
	if alien['colour'] == 'green':
		alien['colour'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'
	elif alien['colour'] == 'yellow':
		alien['colour'] = 'red'
		alien['points'] = 15
		alien['speed'] = 'fast'

for alien in aliens[:5]:
	print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")