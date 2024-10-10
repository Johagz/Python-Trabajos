#Crear un Diccionario
persona={
    "Nombre":"Alejandra",
    "Edad": 30,
    "Ciudad": "Merida"
}

#Usamos el metodo

pares_clave_valor=persona.items()

#Imprimir
print("pares clave valor:", pares_clave_valor)

#Convertir Valores en una lista
valores_lista=list(pares_clave_valor)
print("Valores como lista", valores_lista)