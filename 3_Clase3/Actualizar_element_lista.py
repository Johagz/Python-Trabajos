#lista inicial
mi_lista=[10,20,30,40,50]
print("lista original: ", mi_lista)


#Actualizar un elemento en especifico
mi_lista[2]= 35
print("lista despues de actualizar el tercer elemento", mi_lista)


#Actualizar un elemento usando indice negativo
mi_lista[-1]= 85
print("lista despues de actualizar el ultimo elemento", mi_lista)

#Actualizar varios elementos usando indice slicing
mi_lista[1:4]= [23,36,45]
print("lista despues de actualizar un rango de elemento", mi_lista)

#Actualizar basado en una condición
for i in range(len(mi_lista)):
 if mi_lista[i]>30:
   mi_lista[i]+=10
print("lista despues de actualizar elementos mayores que 30: ", mi_lista)  
 