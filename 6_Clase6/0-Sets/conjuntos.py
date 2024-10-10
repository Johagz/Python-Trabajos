#Función agregar .add()
mi_conjunto={1,2,3}
mi_conjunto.add(4)
print(mi_conjunto)
print("si coloco el numero 1 que ya existe ¿que pasa?")
mi_conjunto.add(1)
print(mi_conjunto) # Si el numeor se encuentra no se agrega de nuevo ya que no permite duplicados 

#Función eliminar .remove()
mi_conjunto1={1,2,3,4}
mi_conjunto1.remove(1) #si remuevo un elemento que no esta me saldra key error
print(mi_conjunto1)

#Elimida con función .discard()
mi_conjunto1={1,2,3,4}
mi_conjunto1.discard(1) #si remuevo un elemento que no esta no arroja error
print(mi_conjunto1)
mi_conjunto1.discard(5) #si remuevo un elemento que no esta no arroja error
print(mi_conjunto1)




#Unión  | 
conjunto1={1,2,3}
conjunto2={3,4,5}
union=conjunto1|conjunto2
print("Imprimo la union del conjunto 1 y conjunto 2: ", union)# no imprime dos veces el tres solo una vez aunque aparesca 2 veces.

#otra forma de escribir es con la sintaxis conjunto.union(conjunto2)
print("Imprimir la union del conjunto con la sintaxis de conjunto.union(conjunto2)")
conjunto3=conjunto1.union(conjunto2)
print(conjunto3)

#Intersección &

interseccion=conjunto1 & conjunto2
print("Imprimo la intersección del conjunto 1 y conjunto 2: ", interseccion)# imprime los numeros que son comunes entre los dos conjuntos 

#Otra forma de escribir la interseccion es con la sintaxis 
print("Interseccion por sintaxis")
interseccion=conjunto1.intersection(conjunto2)
print(interseccion)


#Diferencia  -
diferencia= conjunto1-conjunto2
print("imprime la diferencia entre dos conjuntos (son los datos que estan en el primer conjunto y no en el segunto segunto)",diferencia)

#Forma de escribir por sintaxis 

dife=conjunto1.difference(conjunto2)
print("Imprime la diferencia por sintaxis:", dife)

#Simetria

simetria=conjunto1.symmetric_difference(conjunto2)
print(f"imprime la simetria: {simetria}")