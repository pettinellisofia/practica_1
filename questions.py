import random
import string

categorias = {
    "estructuras": ["cadena","lista", "funcion"],
    "conceptos": ["python","programa", "variable", "entero"]
}

print("¡Bienvenido al Ahorcado!")
print(f"Categorias: estructuras, conceptos")

opcion = input("Elegi una categoria: ").lower()
if opcion not in categorias:
    opcion = "conceptos"

words = categorias[opcion]

palabras_mezcladas = random.sample(words,len(words))

word = palabras_mezcladas[0]

guessed = []
attempts = 6
puntaje = 0

print()

while attempts > 0:
    progress = " ".join([letter if letter in guessed else "_" for letter in word])
    print(progress)
# Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        puntaje += 6
        print(f"¡Ganaste! Tu puntaje final es: {puntaje}")
        break

    print(f"Intentos restantes: {attempts} | Puntaje actual: {puntaje}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ").lower() ## uso lower para convertir mayus en minus para evitar error ##

    if len(letter) != 1 or not letter in string.ascii_letters:
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