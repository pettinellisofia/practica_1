n = int(input("ingresa hasta qué numero contar:"))

for i in range(1, n+1):
    if i%5==0:
        continue
    print(i)