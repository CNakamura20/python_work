#teste de igualdade ou não igualdade
color = 'Red'

if color != 'Red':
	print("false")
else:
	print("true")

#teste usando a função lower
color.lower() == 'red'
print(color)

#teste númericos
print('carol' == 'bruno')
print('carol' != 'bruno')
print('carol' > 'bruno')
print('carol' < 'bruno')
print('carol' >= 'bruno')
print('carol' <= 'bruno')

#teste usando as palavras and e or
age_1 = 20
age_2 = 21

print((age_1<23) and (age_2>=21))
print((age_1 <10) or (age_2<20))

#teste para verificar se um item está em uma lista
favorite_foods = ['sorvete', 'chocolate', 'batata']
food = 'banana'
if food in favorite_foods:
	print("Está na lista")
else:
	print("Não está na lista")
	
#teste para verificar se um item está na lista
favorite_foods = ['sorvete', 'chocolate', 'batata']
food = 'banana'
if food not in favorite_foods:
	print("Não está na lista")
else:
	print("Está na lista")
