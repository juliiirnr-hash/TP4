#Ejercicio4.2
# Sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores

while True:
    numero1 = int(input("Ingrese un número entero (positivo o negativo): "))
    numero2 = int(input("Ingrese otro número entero (positivo o negativo): "))

    if numero1 >= numero2:
        mayor = numero1
        menor = numero2
    else:
        mayor = numero2
        menor = numero1

    suma = 0
    # Cálculo de la suma de los números entre los dos valores dados, excluyendo
    for i in range(menor + 1, mayor):
        suma += i
        print(suma)

    print(f"La suma de los números entre {numero1} y {numero2} es: {suma}")
    pregunta = input("¿Desea ingresar otro par de números? (s/n u otra letra): ").lower()
    if pregunta != "s":
        break

    
 