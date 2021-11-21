#lista
coutries = ['brasil', 'japão', 'coreia do sul', 'frança', 'alemanha']
print(coutries)

# chamando item e criando mensagem
print(coutries[3].title())
message = "Eu quero visitar " + coutries[3].title() + " algum dia."
print(message)

#modificando elemento
coutries[0] = 'emirados árabes unidos'
print(coutries)

#concatenação
coutries.append('brasil')
print(coutries)

#inserindo elemento
coutries.insert(0, 'bulgária')
print(coutries)

#remoção de item com del
del coutries[1]
print(coutries)

#removendo item com pop()
popped_coutries = coutries.pop(4)
print(coutries)
print(popped_coutries)

#removendo item de acordo com  valor
coutries.remove('frança')
print(coutries)

#organizando lista permanente com sort()
coutries.sort()
print(coutries)

#ordem reversa de sort()
coutries.sort(reverse=True)
print(coutries)

#organizando lista temporariamente com sorted()
print(sorted(coutries))

#lista em ordem inversa
print(coutries)
coutries.reverse()
print(coutries)

#tamanho de uma lista
print(len(coutries))





