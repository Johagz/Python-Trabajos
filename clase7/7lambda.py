suma = lambda x,y: x+y
print(f"Suma de 5 y 3: {suma(5,3)}")

#Ejemplo usando map()

numeros=[1,2,3,4,5]
cuadrados=map(lambda x:x**2, numeros)
print(f"Cuadrados de la lista: {numeros}:{list(cuadrados)}")

#Ejemplo Usando filter()
numeros2=[1,2,3,4,5]
pares = filter(lambda x: x%2==0, numeros)
print(f"numeros pares de la lista: {numeros2}:{list(pares)}")

#Ejemplo usando Sorted()
tuplas=[(1,2),(3,4),(5,0)]
ordenadas= sorted(tuplas, key=lambda t: t[1])
print(f"lista de tuplas ordenadas por el segundo elemento : {ordenadas}")
