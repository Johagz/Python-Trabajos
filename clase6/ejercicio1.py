#""" 1. Ejercicio de Sets y for 
#Crea un programa que reciba una lista de números y realice las siguientes 
#operaciones: 
#1. Crear un set a partir de la lista para eliminar duplicados. 
#2. Iterar sobre el set e imprimir cada número. 
#3. Contar cuántos números son mayores que un valor dado y almacenarlos en un nuevo set.


#Ejercicio 1 Sets y For
lista=[1,2,3,4,5,6,7,1,3,4,12,34]
print(f"La lista original es: {lista}")
mi_conjunto=set(lista)
print(f"Eliminamos duplicados creando un conjunto {mi_conjunto}")

print("Los Elementos del Conjunto son: ")
for elemento in mi_conjunto:
     print(elemento)
     nuevo_conjunto=set()
     for elemento in mi_conjunto:
         if elemento > 5:
             nuevo_conjunto.add(elemento) 
           
print(f"El nuevo conjunto esta compuesto por los números del primer conjunto que son mayores que 5:{nuevo_conjunto}")       
        

        
        
    
        

              
       


