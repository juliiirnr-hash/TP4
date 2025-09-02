##Ejercicio4.8.2
#Escribe un programa que permita al usuario ingresar 100 números enteros. 
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son 
#positivos. 
#En este caso se plantera el mismo problema que en el ejercicio anterior, pero sin la opción de que el usuario decida dejar de ingresar números antes de llegar a 100.
pares=0
impares=0
negativos=0
positivos=0
cero=0
intentos=0
for intentos in range(100):
    numero=int(input("Ingrese un número entero: "))
    if numero%2==0:
        pares+=1
    else:
         impares+=1
    if numero<0:
         negativos+=1
    elif numero==0:
         cero+=1
    else:
         positivos+=1
  
print(f"De los números ingresados, {pares} es/son pare/s, {impares} es/son impare/s, {negativos} es/son negativo/s, {positivos} es/son positivo/s y {cero} es/son ceros.")