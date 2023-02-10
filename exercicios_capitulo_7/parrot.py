#message = input(" tell me something, and i will repeat it back to you:")
#print(message)

prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end yhe program."

active = True
while active:
	message = input(prompt)
	
	if massage == 'quit':
		active = False
	else:
		print(message)

#message = ""
#while message != 'quit':
#	message = input(prompt)
	
#	if message != 'quit':
#		print(message)
