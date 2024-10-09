#Cear una tupla con varios elementos
mi_tupla=(10,20,30,40,50)

#Encontarar el numero 30 en la tupla

indice_de_30= mi_tupla.index(30)
print(f"el numero 30 se encuentra en la posición {indice_de_30} de la tupla")

#Verificar si un valor esta em la tupla antes de buscar su indice

valor_buscado=50
if valor_buscado in mi_tupla:
    #si valor buscado esta en la tupla buscar su indice
    indice_del_valor=mi_tupla.index(valor_buscado)
    print(f"El numero {valor_buscado} se encuentra en la posición {indice_del_valor} de la tupla")
else:
    #si el valor no esta, mostrar un mensaje 
    print("El Valor buscado no esta en la tupla")
    