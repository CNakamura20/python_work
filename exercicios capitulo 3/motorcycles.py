motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#mudar coisas
motorcycles[0] = 'ducati'
print(motorcycles)
#inserir coisas
motorcycles.append('ducati')
print(motorcycles)
#inserir um por um dento de uma lista
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
#adicionar coisas de acordo com a posição
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
#deletar coisas
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

#pop, removendo itens para modifica-los depois 

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

#exemplo

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop(0)
print("the last motorcycle I owned was a " + last_owned.title() + ".")

#metódo remove

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")



