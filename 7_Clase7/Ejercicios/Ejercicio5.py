#Ejercicio de for con enumerate y break/continue
Nombres=["Marta","José","Camilo","Ana","Carlos"]
lista=[]
for  indice,nombre in enumerate(Nombres):
    if nombre[0]=="A":
        continue
    elif nombre=="Carlos":
        print(f"Se encontro en el indice {indice} a {nombre}")
        break
    else:
        print(f"Los elementos tiene los siguientes indices y nombres: {indice}: {nombre}")
        
