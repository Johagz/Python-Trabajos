#Crear una Tupla
tupla_mixta=(1,"hola", 3.5)

#Mostrar Tupla
print("Tupla completa: ", tupla_mixta)

#Acceder a los elementos de la tupla por su indice (posición)
print("Primer elemento de la tupla: ", tupla_mixta[0])
print("segundo elemento de la tupla: ", tupla_mixta[1])
print(" Tercer elemento de la tupla: ", tupla_mixta[2])

#Explicación tuplas inmutables
print("\nlas Tuplas no se pueden modificar")

print("\nIntentemos cambiar un elemento de una tupla para ver el error resultante")

#tupla_mixta[0]=10

#Explicación Clara de la Inmutabilidad
print("Si la tupla_mista [0]= 10, python dira que no se puede cambiar un elemento de una tupla")

#Mostramos como si podemos "modificar" una tupla, creando una nueva tupla

tupla_mixta=(10,"hola",3.5)
print("Nueva tupla con el primer elemento cambiado: ",tupla_mixta)
print("tupla original permanece sin cambios: ", tupla_mixta)
