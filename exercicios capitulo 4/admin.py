users = ['admin', 'carol', 'bruno', 'helena', 'rafael']
if users:
	for user in users:
		if user == 'admin':
			print("Olá adimin, gostaria de ver um relatório de status?")
		else:
			print("Seja bem-vindo(a) " + user.title() + ".")
else:
	print("Precisamos encontrar alguns usuários!")		

	
		
		
		
