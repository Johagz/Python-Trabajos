#Ejercicio 3: Anidación Básica de Diccionarios 
#1. Crea un diccionario que represente una persona con las siguientes 
#claves: 
#o Nombre 
#o Edad 
#o Dirección (donde la dirección es otro diccionario con claves: 
#Calle, Ciudad, Código postal) 
#2. Imprime la ciudad de la dirección.

#Ejercicio 3: Anidación Básica de Diccionarios 

Persona={
    "Nombre": "Maria",
    "Edad":29,
    "Direccion":{
        "calle":"Miranda",
        "Ciudad":"Caracas",
        "Codigo postal":"1000"
    }
}
print("El nombre de la Ciudad es: ", Persona["Direccion"]["Ciudad"])