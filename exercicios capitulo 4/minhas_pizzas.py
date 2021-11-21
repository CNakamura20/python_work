pizzas = [ 'chocolate', 'milho', 'brócolis']
friend_pizzas = pizzas[:]

pizzas.append('sorvete')
friend_pizzas.append('marguerita')

print("Minhas pizzas favoritas são:")
for pizza in pizzas[:]:
	print(pizza.title())
	
print("\nAs pizzas favoritas do meu namorado são:")
for friend_pizza in friend_pizzas[:]:
	print(friend_pizza.title())



