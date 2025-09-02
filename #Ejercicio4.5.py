#Ejercicio4.5
#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
numero_aleatorio = random.randint(0, 9)  # Número entre 0 y 9, ambos incluidos
intentos = 0
while True:
    numero_solicitado=int(input("Adivina el número (entre 0 y 9): "))
    #Validacion de entrada
    if numero_solicitado < 0 or numero_solicitado > 9:
        print("Por favor, ingrese un número válido entre 0 y 9.")
        continue
    intentos += 1
    if numero_solicitado==numero_aleatorio:
        print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos.")
        break
    else:
        print("Número incorrecto. Intenta de nuevo.")
    
