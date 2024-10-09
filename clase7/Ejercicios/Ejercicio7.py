#Ejercicio Combinado 
import random
list=[]
list1=[]
list2=[]
for i in range(1,21):
    n =random.randrange(1,20)
    list.append(n)
    if i==20:
        for elemento in list:
           if elemento <10:
               list1.append(elemento)
               continue
           elif elemento%15==0:
               list2.append(elemento)
               break
           else:
               no_cumple=[elemento for elemento in list if elemento>10 or elemento%15 != 0]

print(f"La Lista de numeros aleatorios es: {list}")
print(f"Los numeros de la lista que son menores que 10 son: {list1}")
print(f"Los numeros de la lista que son divisibles por 15 son: {list2}")
print(f"Los numeros de la lista que no cumplen ninguna condicion son:{no_cumple}")