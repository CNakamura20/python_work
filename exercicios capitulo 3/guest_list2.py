#primeira lista de convidados
guest_list = ['midori', 'genaro', 'iago']
print(guest_list)

message = "Com muito prazer gostaria de convidar você, " + guest_list[0].title() + ", para um jantar em minha casa."
print(message)
message = "Olá, " + guest_list[1].title() + ", gostaria de jantar em minha casa hoje?"
print(message)
message = "Te liga só, " + guest_list[2].title() + " vai ter um jantar hoje lá em casa, topa?"
print(message)

#segunda lista de convidados
guest_list[1] = 'jimin'
print(guest_list)

message = "Com muito prazer gostaria de convidar você, " + guest_list[0].title() + ", para um jantar em minha casa."
print(message)
message = "Olá, " + guest_list[1].title() + ", gostaria de jantar em minha casa hoje?"
print(message)
message = "Te liga só, " + guest_list[2].title() + " vai ter um jantar hoje lá em casa, topa?"
print(message)
