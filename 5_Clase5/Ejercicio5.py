#Ejercicio 5: Diccionario dentro de una Lista 
#1. Crea una lista de diccionarios donde cada diccionario representa un 
#producto en una tienda, con claves: 
#o Nombre 
#o Precio 
#o Cantidad en stock 
#2. Imprime el nombre y el precio del segundo producto en la lista. 

#Ejercicio 5: Diccionario dentro de una Lista 

lista_de_productos=[{"Nombre":"Lamparas","Precio":20,"Cantidad en Stock":10},{"Nombre":"Computadoras","Precio":350,"Cantidad en Stock":50},{"Nombre":"Teclados","Precio":10,"Cantidad en Stock":60}]

print(f"El Segundo Producto en la lista son: {lista_de_productos[1]["Nombre"]} y tienen un costo de: {lista_de_productos[1]["Precio"]} ")
