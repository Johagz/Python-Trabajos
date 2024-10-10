#Ejercicio 4: Manipulación de Tuplas y Comprobación de indices
Frutas=("Manzana","Banana","Cereza")
indice = Frutas.index("Banana")
print(f"La Banana se encuentra en la posición {indice} de la tupla")

Fruta_buscada="Naranja"
if Fruta_buscada in Frutas:
    print(f"La {Fruta_buscada} se encuentra en la tupla")
else:
     print(f"La {Fruta_buscada} no esta en la tupla")
