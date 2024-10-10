#Crear diccionario
persona={
    "Nombre":"Alejandra",
    "Edad": 30,
    "Ciudad": "Merida",
    "profesion": "profe"
}

print("diccionario original", persona)

#Usamos popitem para eleminar y obtener el ultimo par clave valor
ultimo_elemento=persona.popitem()
#imprimir

print("Ultimo valor eliminado", ultimo_elemento) 
print("Diccionario despues de usas popitem()", persona) 
