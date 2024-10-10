#Definición de listas

mi_lista=["a","b","c","d"]

#Acceso usando indices positivos

primer_elemento= mi_lista[0]
print("Tu primer elemento de la lista es:" , primer_elemento)

#Segundo elemento
segundo_elemento= mi_lista[1]
print("Tu segundo elemento de la lista es:" , segundo_elemento)

#Ultimo elemento
ultimo_elemento= mi_lista[-1]
print("Tu ultimo elemento de la lista es:" , ultimo_elemento)

# Acceder a sublista (slicing)
print("sublista (indice 1 a 3)", mi_lista[1:4])
print("sublista (inicio a 3)", mi_lista[:3])
print("sublista (indice 2 a final)", mi_lista[2:])

# Acceder a sublista con paso 2 (slicing)
print("sublista con paso 2 (indice 1 a 3)", mi_lista[1:4])
print("sublista (inicio a 3)", mi_lista[:3])
print("sublista (indice 2 a final)", mi_lista[2:])