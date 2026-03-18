p = input("ingresa palabras separadas por espacio: ")
palabras = p.split( )
palabras_largas = []
for i in palabras:
    if len(i) > 3:
        palabras_largas.append(i)

result = " ".join(palabras_largas)
print(f"oracion final: {result}")