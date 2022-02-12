current_users =['carol', 'bruno', 'jamile', 'silvane', 'adair']
new_users = ['carla', 'carol', 'BRUNO', 'rafael', 'sara']

for new_user in new_users:
	if new_user.lower() in current_users:
		print("Desculpe " + new_user + " você deve fornecer um novo nome de usuário!")
	else:
		print("O usuário " + new_user + " está disponível.")
#pedir ajuda para o nego veio ver se está certo.

