#Ejercicio 4: Lista de Diccionarios 
#1. Crea una lista de diccionarios, donde cada diccionario representa un 
#estudiante con las siguientes claves: 
#o Nombre 
#o Edad 
#o Calificaciones (que es una lista de números) 
#2. Imprime el nombre y las calificaciones del primer estudiante en la lista.

#Ejercicio 4: Lista de Diccionarios 
lista_alumnos=[{"Nombre":"Pedro","Edad":12,"Calificaciones":[12,13,20,10]},{"Nombre":"Mariana","Edad":13,"Calificaciones":[18,10,19,15]},{"Nombre":"Julian","Edad":11,"Calificaciones":[10,16,14,18]}]

print("El primer estudiante en la lista se llama: ", lista_alumnos[0]["Nombre"])
print(f"Las Calificaciones de {lista_alumnos[0]["Nombre"]} son: ", lista_alumnos[0]["Calificaciones"])
