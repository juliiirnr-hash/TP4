#calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
numero=int(input("Ingrese un número entero positivo: "))
#Asegurarse de que el número sea positivo
while numero<0:
    numero=int(input("Número inválido. Ingrese un número entero positivo: "))

suma=0

for i in range(0,numero):
   suma+=i
print(f"La suma de todos los números entre 0 y {numero} es: {suma}")