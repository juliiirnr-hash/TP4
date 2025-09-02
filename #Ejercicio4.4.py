#Ejercicio4.4
#permita al usuario ingresar números enteros y los sume en secuencia.
#El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

suma=0 #acumulador
#ciclo para solicitar números y sumar
while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
  # Si el número es 0, salir del ciclo
    if numero == 0:
        break
    suma += numero
    #Para ver la suma parcial en cada paso, descomente la siguiente línea:
    print(f"Suma parcial: {suma}")
print(f"La suma total es: {suma}")