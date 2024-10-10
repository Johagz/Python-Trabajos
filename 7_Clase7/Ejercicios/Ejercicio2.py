#Ejercicio Integrador
numeros_sin_condicion= set() 
for i in range(1,21):
    if i%3==0:
        continue
    elif i>15:
        break
    else:
       numeros_sin_condicion.add(i)

print(f"Los numeros que no son divisibles entre 3 y son menores que 15 son los siguientes: {numeros_sin_condicion}")
pares=set()
for n in numeros_sin_condicion:
    if n%2==0:
        pares.add(n)
        
print(f"De los numeros mostrados anteriormente los pares son: {pares}")