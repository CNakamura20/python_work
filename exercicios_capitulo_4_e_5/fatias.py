foods = ['pizza', 'lasanha', 'sorvete', 'pastel', 'lentilha']

print("Os três primeiros itens da lista são:")
for food in foods[:3]:
	print(food)


print("\nTrês itens do meio da lista são:")
for food in foods[1:4]:
	print(food)

print("\nOs três últimos itens da lista são:")
for food in foods[2:]:
	print(food)
