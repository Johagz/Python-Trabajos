#Crear un Diccionario
peresona={
    "nombre": "Analia",
    "Edad": 36,
    "Ciudad":"Colon-Entre Rios"
}

#Usamos el Método .values()
valores=peresona.values()

#Imprimimos

print("Los Valores del Diccionario:", valores)

#Convertir Valores en una lista
valores_lista= list(valores)
print("Valores como lista: ", valores_lista)