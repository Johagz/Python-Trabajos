#Definir una matriz de 3x3

matriz=[
    [1,2,3], #fila 0
    [4,5,6], #fila 1
    [7,8,9] #fila 2
]

#Acceder y mostrar algunos elementos especificos de la matriz

print("Algunos elementos de la matriz")
print("Elementos en la Fila 0, Columna 0: ",matriz[0][0])

print("Elemenros en la Fila 0, Columna 1: ", matriz[0][1])

#Modificar elementos especificos de una matriz

print("\n Modificando elemento especifico: ")
matriz[0][1]=10 #Cambiar el elemento en la fila 0, columna 1 a valor 10
matriz[2][0]=15 #Cambiar el elemento en la fila 2, columna 0 a valor 15
print(matriz)


#Acceder a una fila completa
print("\n Accediedo a una fila completa:")
fila_completa=matriz[1] #obtener la fila completa
print("Fila completa en la posición 1: ",fila_completa)

#Reemplazar una fila completa
print("\n Reemplazar una fila completa: ")
matriz[1]=[20,21,22]
print("matriz despues de reemplazar la fila 1")
print(matriz) 


#trabajar con una submatriz (parte de una matriz)
submatriz= [matriz[0][1:3], matriz[1][1:3]] #extrae submatriz de las columnas 1 a 2 de las filas de 0 y 1
print("submatriz estraida: ", submatriz)

#Mostramos toda la matriz al final 
print("\nMatriz completa al final")
print(matriz[0])
print(matriz[1])
print(matriz[2])


