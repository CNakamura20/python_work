#armazena informações sobre uma pizza que está sendo pedida
pizza = {
	'crust': 'thick',
	'toppings':['mushrooms', 'extra cheese'],
	}
	
#resume o pedido
print(" you ordered a " + pizza['crust'] + "-crust pizza" + "with the following toppings:")
	
	
for topping in pizza['toppings']:
	print("\t" + topping)
	
	
	
