total = 0

while True:
    precio = float(input("ingresa el precio del producto: "))
    if precio == 0:
        break
    total += precio

print(f"el total acumulado es: {total}")