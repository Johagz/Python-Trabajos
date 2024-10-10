#Ejercicio 3: Suma de Sublistas 
#Crea un programa que tome una lista de números y calcule la suma de una 
#sublista especificada por el usuario. 
#Instrucciones: 
#• Define una lista de números predefinida. 
#• Pide al usuario que ingrese el índice de inicio y el índice de fin para 
#la sublista. 
#• Usa slicing para obtener la sublista. 
#• Suma los elementos de la sublista. 
#• Muestra la suma.



#Ejercicio 3: Suma de Sublistas 
lista_numero=[10,20,30,40,50,60,70,80]
print("Los Indices que ingrese deben ser números entre 0 y 8")
indice_inicio=int(input("Ingrese el indice de inicio de la sublista: "))
indice_final=int(input("Ingrese el indice final de la sublista: "))
lista_definida= lista_numero[indice_inicio:indice_final]
suma= sum(lista_definida)
print(f"La lista original es: {lista_numero}")
print(f"La lista definida por el Usuario es: {lista_definida} ")
print(f"La Suma de los elementos de la lista definida es igual a : {suma}")



