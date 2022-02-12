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

#reduzindo a lista de convidados
message = "Nossa mesa de jantar não chegará a tempo, então receio que só poderei receber apenas dois convidados"

print(guest_list)

person1 = guest_list.pop(0)
print("Peço desculpas pelo jantar " + person1.title() + ".")
person2 = guest_list.pop(1)
print("Desculpa o jantar não dar certo " + person2.title() + ".")
person3 = guest_list.pop(2)
print("Não vai rolar o jantar hoje espero que não se importe " + person3.title() + ".")
person4 = guest_list.pop(2)
print("Desculpe pelo imprevisto do jantar " + person4.title() + ".")

print(guest_list)

del guest_list [0]
del guest_list [0]

print(guest_list)

print(len(guest_list))
                                




