#Ejercicio 6: Anidación Compleja de Diccionarios y Listas 
#1. Crea un diccionario que contenga información sobre una escuela. La escuela tiene: 
#o Nombre 
#o Año de fundación 
#o Lista de clases, donde cada clase es un diccionario con: 
#▪ Nombre de la clase 
#▪ Lista de estudiantes, donde cada estudiante es un diccionario con: 
#▪ Nombre 
#▪ Edad 
#2. Imprime el nombre del primer estudiante de la primera clase.

#Ejercicio 6: Anidación Compleja de Diccionarios y Listas
lista_de_escuela={
    "Nombre":"Refugio de la Infancia",
    "Año de Fundación":1970,
    "Lista de Clases":[
        {"Nombre de la Clase":"Religión",
         "Lista de estudiantes":
             [{"Nombre del estudiante":"Matias", "Edad":12},{"Nombre del estudiante":"Marta", "Edad":11},{"Nombre del estudiante":"Jose", "Edad":11}]},
        {"Nombre de la Clase":"Matematica",
              "Lista de estudiantes":[{"Nombre del estudiante":"Juan", "Edad":15},{"Nombre del estudiante":"Manuel", "Edad":16},{"Nombre del estudiante":"Laura", "Edad":15}]},
        {"Nombre de la Clase":"Castellano",
              "Lista de estudiantes":[{"Nombre del estudiante":"Luis", "Edad":12},{"Nombre del estudiante":"Pepe", "Edad":11},{"Nombre del estudiante":"Rosalia", "Edad":10}]}
]}
print(f"El primer estudiante en la lista de la primera Clase se LLama: {lista_de_escuela["Lista de Clases"][0]["Lista de estudiantes"][0]["Nombre del estudiante"]} ")















