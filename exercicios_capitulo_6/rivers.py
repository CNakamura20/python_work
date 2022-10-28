rivers = {
	'ganges': 'índia',
	'congo': 'áfrica',
	'volga': 'rússia',
	}
	
for key, river in rivers.items():
	print("o " + key.title() + " corre pela " + river.title() + ".")

for key, river in rivers.items():
	print(key.title() + ": " + river.title())
