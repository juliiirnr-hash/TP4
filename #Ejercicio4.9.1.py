#Ejercicio4.9
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores
suma=0
n=0
for i in range(100):
    numero=int(input("Ingrese un número entero: "))
    suma+=numero
    n+=1
   

mean=suma/n
print(f"La media de los números ingresados es:{mean}")

