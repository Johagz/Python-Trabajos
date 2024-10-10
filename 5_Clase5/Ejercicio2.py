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

#Ejercicio 2: Modificar y Eliminar Elementos de un Diccionario 
#1. Usando el diccionario del ejercicio anterior, actualiza el año de 
#publicación a 1968. 
#2. Elimina el género del diccionario. 
#3. Imprime el diccionario después de cada operación. 

#Ejercicio 2: Modificar y Eliminar Elementos de un Diccionario 

estanteria["Año de Publicacion"]=1968
print("Se actualizo el año de publicación:")
print("Los Datos con el cambio en el año de publicación: ",estanteria)
elimina_genero=estanteria.pop("Genero")
print("Se elimino el Genero", estanteria)

