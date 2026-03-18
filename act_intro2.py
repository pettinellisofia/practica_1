segundos_totales = int(input("ingresa una cantidad de segundos: "))

horas = segundos_totales//3600
minutos = (segundos_totales%3600)//60
segundos = segundos_totales%60

print(f"{segundos_totales} segundos son {horas} horas, {minutos} minuto y {segundos} segundos.")