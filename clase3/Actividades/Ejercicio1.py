#Ejercicio 2: Contador de Números Específicos 
#Escribe un programa que cuente cuántas veces aparece un número 
#específico en una lista. 
#Instrucciones: 
#• Define una lista de números predefinida o pídele al usuario que 
#ingrese los números. 
#• Pide al usuario que ingrese un número a buscar.  
#3• Usa el método count() para determinar cuántas veces aparece el 
#número en la lista. 
#• Muestra el resultado. 



# Ejercicio 2: Contador de Números Específicos 
lista=[1,2,3,4,2,5,2,6,2,11,23,11,4]
print("Lista de Números: ", lista)
buscar= int(input("Ingrese el Número que desea contar en la lista: "))
conteo= lista.count(buscar)
print(f"El número {buscar} aparece {conteo} veces en la lista")



