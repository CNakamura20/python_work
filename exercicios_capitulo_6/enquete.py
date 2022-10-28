favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
	
enquete = ['jen', 'sarah', 'edward', 'phil', 'carol', 'bruno']
for enquete in favorite_languages.keys():
	print(enquete.title() + " thank you for participating in the poll!")
	
	if favorite_languages not in enquete:
		print(enquete.title() + " please take our poll!")
