#Ejercicio 1: Crear y Acceder a un Diccionario Básico 
# Crea un diccionario que contenga la siguiente información sobre un 
#libro: 
# Título 
# Autor 
# Año de publicación 
# Género 
#2 Accede e imprime cada uno de estos valores usando las claves correspondientes. 

#Ejercicio 1: Crear y Acceder a un Diccionario Básico 

estanteria={
    "Titulo":"El Principito",
    "Autor":"Atoine de Saint",
    "Año de Publicacion": 1943,
    "Genero":"No pertenece a un genero determinado"
}

print("Titulo del Libro: ", estanteria["Titulo"])
print("Autor del Libro: ", estanteria["Autor"])
print("Año de Publicación del Libro: ", estanteria["Año de Publicacion"])
print("Genero del Libro: ", estanteria["Genero"])
