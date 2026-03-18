n = int(input("ingresa hasta qué numero contar:"))
multiplos = []
otros = []

for i in range(1, n+1):
    if i%5==0:
        multiplos.append(i)
    else:
        otros.append(i)

print(f"multiplos de 5: {multiplos}")
print(f"resto de los numeros: {otros}")