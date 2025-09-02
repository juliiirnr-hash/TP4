#Ejercicio4.8.1
#Escribe un programa que permita al usuario ingresar 100 números enteros. 
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son 
#En este caso se plantera el problema permitiendo al usuario decidir si desea continuar ingresando números después de cada entrada, una vez que haya ingresado al menos 5 números.
#Inicialización de contadores
pares=0
impares=0
negativos=0
positivos=0
cero=0
intentos=0

while intentos<100:
    numero=int(input("Ingrese un número entero: "))
    intentos+=1
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
  
    if intentos>5 and intentos<100:
       pregunta=input("¿Desea ingresar otro número? (s/n u otro): ").lower()
       if pregunta!="s":
              break
   
 
print(f"De los números ingresados, {pares} es/son pare/s, {impares} es/son impare/s, {negativos} es/son negativo/s, {positivos} es/son positivo/s y {cero} es/son ceros.")