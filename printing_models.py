# unprinted_models = ['phone case', 'toy', 'watch cover']
# printed_models = []

# while unprinted_models:
# 	current_model = unprinted_models.pop()
# 	print(f"Printing model: {current_model}")
# 	printed_models.append(current_model)
# print(f"\nThe following models have been printed")
# for printed_model in printed_models:
#  	print(printed_model)


def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""shows completed modelss"""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['phone case', 'toy', 'watch cover']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
print("\n---***---\n")

# the slice makes a copy of the list

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)