#Ejercicio4.6
#Desarrollar un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for numero in range(100,-1,-1):
    if numero%2==0:
        print(numero)
#El ciclo for recorre los números del 100 al 0 (en orden decreciente) y el condicional if verifica si el número es par (es decir, si el resto de la división por 2 es cero). Si es par, se imprime en pantalla.
