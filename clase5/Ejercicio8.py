#Ejercicio 8: Modificar un Valor en un Diccionario Anidado 
#1. Crea un diccionario que contenga información sobre una tienda de libros, con las siguientes claves: 
#o nombre_tienda 
#o libros, que es una lista de diccionarios, donde cada diccionario representa un libro con claves titulo y precio. 
#2. Cambia el precio del segundo libro en la lista a un nuevo valor (por ejemplo, 15.99). 
#3. Imprime el título y el precio del segundo libro después de la modificación.

#Ejercicio 8: Modificar un Valor en un Diccionario Anidado 

tienda={
    "Nombre_Tienda":"Libreria de los mil Viajes",
    "Libros":[{"Titulo":"Noches Blancas","Precio":18},{"Titulo":"Dracula","Precio":16},{"Titulo":"Cien años de soledad","Precio":10}]   
}

tienda["Libros"][1]["Precio"]= 15.99
print(f"El Nombre del segundo libro es: {tienda["Libros"][1]["Titulo"]} y su precio es: {tienda["Libros"][1]["Precio"]}")

