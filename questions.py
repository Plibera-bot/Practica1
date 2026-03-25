import random
words = {
    "animales":["perro","gato","leon","tigre"],
    "lenguajes de programacion": ["python","java","c","javaScript"],
    "estructuras de datos":["lista","cadena","diccionario"],
    "tipo de dato":["entero","real","string","boolean","char"]
}
puntaje=0
jugar = "si"
words_disponibles={}
for categoria in words:
    words_disponibles[categoria]=words[categoria].copy()
for categoria in words_disponibles:
    words_disponibles[categoria]= random.sample(words_disponibles[categoria],len(words_disponibles[categoria]))
print("¡Bienvenido al Ahorcado!")
print()
while (jugar == "si"):
    while True:
        print(words.keys())
        categoria=input("elegi una categoria: ").lower()
        if(categoria in words):
            if(len(words_disponibles[categoria])==0):
                print("no quedan palabras en esta categoria, elegi otra.")
                continue
            word=words_disponibles[categoria].pop()
            break
        else:
            print("categoria invalida, intenta de nuevo")
    guessed = []
    attempts = 6

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
            jugar = input("quiere seguir jugando? si/no: ")
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
        jugar = input("quiere seguir jugando? si/no: ")