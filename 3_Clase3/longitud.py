#Longitud listas 
#longitud de una lista vacia 

lista_vacia=[]
print("longitud de un lista vacia: ", len(lista_vacia))

#lista con enteros 
#la longitud es igual al numero de elementos que tiene la lista

lista_enteros=[1,2,3,4,5]
print("longitud de una lista de enteros es de: ", len(lista_enteros))

#lista con cadenas 
#la longitud es igual al numero de elementos que tiene la lista

lista_cadenas=["manzana","pera","limon","naranja","mango"]
print("longitud de una lista de cadenas es de: ", len(lista_cadenas))

#lista mixta
#la longitud es igual al numero de elementos que tiene la lista sin importar el tipo de elemento (si tiene un anidado de listas se cuenta como un elemento)

lista_mixta=["manzana",23,"limon",34.5,[1,2,3],"mango"]
print("longitud de una lista de mixta es de: ", len(lista_mixta))


