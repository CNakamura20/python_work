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

#mais convidados
message = " Encontramos uma mesa maior por isso teremos mais três convidados, neste jantar"
print(message)

print(guest_list)
guest_list.insert(0, 'mandy')
guest_list.insert(3, 'lohgann')
guest_list.append('prit')
print(guest_list)

message = "Com muito prazer gostaria de convidar você, " + guest_list[0].title() + ", para um jantar em minha casa."
print(message)
message = "Olá, " + guest_list[1].title() + ", gostaria de jantar em minha casa hoje?"
print(message)
message = "Te liga só, " + guest_list[2].title() + " vai ter um jantar hoje lá em casa, topa?"
print(message)
message = "Vai ter um jantar super legal hoje na minha casa, " + guest_list[3].title() + " quer vir?"
print(message)
message = "Vou fazer uma janta super tri, " + guest_list[4] + " aparece por lá."
print(message)
message = "Vou fazer uma janta lá em casa, " + guest_list[5] + " gostaria muito que você fosse."
print(message)


