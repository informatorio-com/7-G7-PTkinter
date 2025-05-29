import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("¡Bienvenido al juego de adivinanza!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        try:
            adivinanza = int(input("Ingresa tu adivinanza: "))
            intentos += 1

            if adivinanza < numero_secreto:
                print("Demasiado bajo. Intenta otra vez.")
            elif adivinanza > numero_secreto:
                print("Demasiado alto. Intenta otra vez.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    '''
    if __name__ == "__main__"
    es una forma estándar en Python de asegurarse de que cierto código solo se ejecute cuando el archivo se ejecuta directamente, y no cuando se importa desde otro archivo.
    ¿Qué significa eso en detalle?

    En Python, cada archivo .py es un módulo. Cada módulo tiene una variable especial llamada __name__.

    Si ejecutas un archivo directamente (por ejemplo, con python juego.py), entonces __name__ se define como "__main__".

    Si importas ese mismo archivo desde otro (por ejemplo, con import juego), entonces __name__ se define como "juego" (o el nombre del archivo).
    
    if __name__ == "__main__":
    ✅ Protege el código para que no se ejecute al importar el archivo.
    ✅ Permite usar el archivo como script principal y como módulo reutilizable.
    '''
    juego_adivinanza()