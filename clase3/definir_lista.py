#Definicion de Litas

#Lista Vacia
lista_vacia=[]
print("Lista Vacia: ", lista_vacia)

#Lista de Elementos Iniciales 

lista_elementos_iniciales =[1,2,3,4,5]
print("Lista Elementos Iniciales: ", lista_elementos_iniciales)
print(f"Lista Elementos Iniciales: {lista_elementos_iniciales}")

#Lista de cadenas de caracteres 

lista_cadenas =["Manzana","Pera","Uva","Limon","Melon"]
print("Lista Elementos Cadenas: ", lista_cadenas)

#Lista Mixta

lista_mixta =[42,"Pera",12.4, ["Limon","Melon"]]
print("Lista Elementos Mixtos: ", lista_mixta)

#Lista con elementos repetidos

lista_repetidos =[0] * 5
print("Lista Elementos repetidos: ", lista_mixta)

#Lista a partir de Otros Iterables
cadena= "hola"
lista_de_caracteres= list(cadena)
print("lista a partir de otros iterables (cadena)", lista_de_caracteres)