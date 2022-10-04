players = ['john', 'paul', 'george', 'ringo', 'brian']
print(players[0:3])
print(players[:4])
print(players[1:5])
print(players[2:])
# print from that number from the end
print(players[-2:])
print(players[-3:])
# third number is a slice, skips that amount in the list
print(players[0:5:2])


print("\nHere are the fist three players in my team:")
for player in players[:3]:
	print(player.title())