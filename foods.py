my_foods = ['pizza', 'burger', 'sushi', 'cake']
friends_foods = my_foods[:]
print("My favourite foods are:")
print(my_foods)
print("My friends favourite foods are:")
print(friends_foods)
my_foods.append('ice cream')
friends_foods.append('crisps')
print("My favourite foods are:")
print(my_foods)
print("My friends favourite foods are:")
print(friends_foods)

# Need the slice in order to copy the contents in the
# list otherwise it treats it as the same variable