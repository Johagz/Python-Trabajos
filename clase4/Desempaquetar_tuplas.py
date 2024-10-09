#Ejemplo de Desempaquetar tuplas

#Crear una tupla con varios tipos de datos
mi_tupla=(1,"python", 3.14)

#Desempaquetar la tupla

numero, lenguaje, pi = mi_tupla
#Mostar el valor de cada variable despues del desempaquetamiento
print("numero: ", numero)
print("lenguaje: ", lenguaje)
print("pi: ", pi)

# Ejemplo 2: numero de variables no coincide con el número de elementos en la tupla

mi_tupla2=(1,"python", 3.14)
#intentar desempaquetar en dos variables (esto causa error)
#numero,lenguaje = mi_tupla2


#Ejemplo 3: Desempaquetado con el operador*
#creamos una tupla
mi_tupla3=(1,"hola", 3.14, "tuplas","desempaquetar")
#Desempaquetar la tupla con el operador * para capturar varios elementos
primer_elemento, *resto= mi_tupla3
print("primer elemento",primer_elemento)
print("resto de los elementos", resto)


