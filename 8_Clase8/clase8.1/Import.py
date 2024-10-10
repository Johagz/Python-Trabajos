#Import Random

import random
print(random.random())

print(random.randint(1,10))

colores= ["rojo","azul","verde"]
print(random.choice(colores)) #Devuelve uno de los colores al azar

numeros=[1,2,3,4,5]
random.shuffle(numeros) #mezcla los numeros
print(numeros)