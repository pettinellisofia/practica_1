import random
words = ["python","programa","variable","funcion","bucle","cadena","entero","lista",]
word = random.choice(words)
guessed = []
attempts = 6

puntaje = 0

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
# Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
# Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        puntaje += 6
        print(f"¡Ganaste! Tu puntaje final es: {puntaje}")
        break

    print(f"Intentos restantes: {attempts} | Puntaje actual: {puntaje}")
    print(f"Letras usadas: {', '.join(guessed)}")

    abc = "abcdefghijklmnñopqrstuvwxyz"
    letter = input("Ingresá una letra: ").lower() ## uso lower para convertir mayus en minus para evitar error ##

    if len(letter) != 1 or not letter not in abc:
        print("Entrada no válida.")
        continue

    if letter in guessed:
        print("Ya usaste esa letra.")
        continue

    if letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        puntaje -= 1
        print("Esa letra no está en la palabra.")
        print()
else:
    puntaje = 0
    print(f"¡Perdiste! La palabra era: {word}")