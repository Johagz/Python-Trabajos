#Crear diccionario
persona={
    "Nombre":"Alejandra",
    "Edad": 30,
    "Ciudad": "Merida"
}

#Usamos pop para 
valor_eliminado= persona.pop("Edad")
print("valor eliminado ", valor_eliminado)

print("Diccionario despues de eliminar edad", persona)

#usar pop con una clave que no existe y un valor por defecto

valor_inexistente=persona.pop("pais", "no especificado")
print(valor_inexistente)