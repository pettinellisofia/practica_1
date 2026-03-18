numero = int(input("ingresa un numero para ver su tabla:"))

print(f"tabla del {numero}:")
for n in range(1,11):
    print(f"{numero} x {n} = {numero * n}")