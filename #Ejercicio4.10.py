#Ejercicio4.10
#) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario.
#  Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero=int(input("Ingrese un número : "))
string_numero=str(numero)
inverso=""
i=len(string_numero)-1
while i>=0:
    if string_numero[i]=="-" :
        inverso="-"+inverso  
        i-=1
    else:
         inverso+=string_numero[i]
         i-=1



        
   

print(f"El número {numero} invertido es {inverso}.")
