# Elimine o corpo da função print_seconds para que ela imprima a 
# quantidade total de segundos, dados os parâmetros da função horas, 
# minutos e segundos. Lembre-se de que existem 3600 segundos em uma 
# hora e 60 segundos em um minuto.

def print_seconds(hours, minutes, seconds):
    hours_in_seconds = 3600 * hours
    minutes_in_seconds = 60 * minutes
    total_seconds = hours_in_seconds + minutes_in_seconds + seconds
    print(total_seconds)

print_seconds(1,2,3)


# Aqui está sua saída: 
# 3723 

# Outro marco em sua experiência de aprendizado. Bem feito!
