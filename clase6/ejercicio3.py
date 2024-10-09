#3. Ejercicio con range, enumerate, y break/continue Escribe un programa que: 
#1. Itere sobre una lista de cadenas usando enumerate para mostrar el índice y el valor. 
#2. Utilice continue para saltar cadenas vacías. 
#3. Utilice break para detener la iteración si se encuentra una cadena con más de 5 caracteres. 

#Ejercico 3 

lista=["Carro","Lima","Perro","Gato","","Lobo","Peluche"]
for indice, valor in enumerate(lista):
    if valor == "":
        continue
    elif len(valor)> 5:
        break
    else:
        print(f"El indice es {indice} y el valor es {valor}")

    
    
    
    
        