import random
words = {
    "animales":["perro","gato","leon","tigre"],
    "lenguajes de programacion": ["python","java","c","javaScript"],
    "estructuras de datos":["lista","cadena","diccionario"],
    "tipo de dato":["entero","real","string","boolean","char"]
}
print(words.keys())
while True:
    categoria=input("elegi una categoria: ").lower()
    if(categoria in words):
        word=random.choice(words[categoria])
        break
    else:
        print("categoria invalida, intenta de nuevo")
guessed = []
attempts = 6

print("¡Bienvenido al Ahorcado!")
print()
puntaje=0
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
        puntaje+=6
        print(f"¡ganaste! y tu puntaje es: {puntaje}")
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ").lower()
    if("a">letter)or("z"<letter)or(len(letter)!=1):
        print("entrada no valida")
        continue

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        puntaje-=1
        print("Esa letra no está en la palabra.")
    print()
else:
    puntaje=0
    print(f"¡Perdiste! La palabra era: {word} y tu puntaje es: {puntaje}")