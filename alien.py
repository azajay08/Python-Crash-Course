from xml.etree.ElementPath import get_parent_map


alien_o = {'colour': 'green', 'points': 5}

print(alien_o['colour'])
print(alien_o['points'])

new_points = alien_o['points']
shot_down = alien_o['colour']
print(f"\nYou have just shot down a {shot_down} alien, You get {new_points} points!\n")

## this will add to dictionary (struct)
alien_o['x_pos'] = 0
alien_o['y_pos'] = 25
print(alien_o)
print("\n\n--------\n\n")

alien_o = {}
print(alien_o)
alien_o['colour'] = 'green'
alien_o['points'] = 5
print(alien_o)
print("\n\n--------\n\n")

alien_o = {'colour': 'green'}
print(f"The alien is {alien_o['colour']}.\n")
## changes key value
alien_o['colour'] = 'yellow'
print(f"The alien is {alien_o['colour']}.\n")
print("\n\n--------\n\n")

## track aliens speed

alien_o = {'x_pos': 0, 'y_pos': 25, 'speed': 'medium'}
print(f"Medium: Original position: {alien_o['x_pos']}\n")

if alien_o['speed'] == 'slow':
	x_increment = 1
elif alien_o['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
alien_o['x_pos'] += x_increment
## long way - alien_o['x_pos'] = alien_o['x_pos'] + x_increment
print(f"Medium: New position: {alien_o['x_pos']}")
print("\n\n--------\n\n")


alien_o = {'x_pos': 0, 'y_pos': 25, 'speed': 'medium'}
## changing speed
alien_o['speed'] = 'fast'
print(f"Fast: Original position: {alien_o['x_pos']}\n")
if alien_o['speed'] == 'slow':
	x_increment = 1
elif alien_o['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
alien_o['x_pos'] += x_increment
print(f"Fast: New position: {alien_o['x_pos']}\n")
alien_o['points'] = 5
## deleting - using 'del'

print("\n\n--------\n\n")
print(alien_o)
print("\nNow delete points:\n")
del alien_o['points']
print(alien_o)
