#Ejercicio 9: Buscar y Imprimir la Edad de un Estudiante en un Diccionario Anidado 
#1. Crea un diccionario que represente una clase con los siguientes datos: 
#o nombre_clase 
#o estudiantes, que es una lista de diccionarios con información de cada estudiante (nombre y edad). 
#2. Escribe una función que busque la edad de un estudiante dado su nombre usando el índice de la lista en lugar de bucles (suponiendo que conoces el índice). 
#3. Imprime la edad del estudiante buscado.

#Ejercicio 9: Buscar y Imprimir la Edad de un Estudiante en un Diccionario Anidado 

clase={
    "nombre_clase":"Python",
    "Estudiantes":[{"nombre":"Juan","edad":16},{"nombre":"Maria","edad":15}]
}

nombre=input("Ingrese uno de estos nombres Juan o Maria: ")
if nombre== "Maria":
    print(f"La Edad de {nombre} es: {clase["Estudiantes"][1]["edad"]} ")
elif nombre == "Juan":
    print(f"La Edad de {nombre} es: {clase["Estudiantes"][0]["edad"]} ")
else:
    print("El nombre ingresado no coincide o se escribio diferente, intentelo nuevamente")
    