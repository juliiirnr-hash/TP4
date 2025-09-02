#Ejercicio4.2
#solicitar al usuario un número entero y determine la cantidad de dígitos que contiene.

while True:
    numero =int(input("Ingrese un número entero: "))
    cantidad_digitos = len(str(abs(numero)))
    print(f"El número {numero} tiene {cantidad_digitos} dígitos.")
    pregunta = input("¿Desea ingresar otro número? (s/n u otra letra): ").lower()
    if pregunta!="s":
        break
#El ciclo while se repite hasta que el usuario decida no continuar.