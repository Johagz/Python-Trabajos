#2. Ejercicio de while y for Desarrolla un programa que haga lo siguiente: 
#1. Usar un bucle while para pedir al usuario que ingrese números hasta que se ingrese el número 0. 
#2. Usar un bucle for para calcular la suma de los números ingresados, excluyendo el 0.


#Ejercicio 2 de while y for

n=1
suma=0

while n != 0:
    n=int(input("Ingrese un número: "))
    lista=[]
    lista.append(n)
    for n in lista:
        suma= suma+n
    
print(f"La suma de los número ingresados es: {suma}")