#Ejemplo Básico de un Generador 
#Generador que produce números del 1 al 5
#Definción del generador 
def contador():
    #itera sobre los números del 1 al 5
    for i in range(1,6):#itera sobre los numeros del 1 al 5 
        yield i #produce el valor de i y pausa la ejecución 

#Crear una instancia para el generador 
gen=contador() # gen es un objeto generador

for numero in gen:
    print(numero) #imprime los números producido por el generador 




    