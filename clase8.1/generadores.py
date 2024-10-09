#Ejemplo Básico de un generador 
#Generador que produce numeros del 1 al 5:
#Definicion del generador 
def contador ():
#Itera sobre los numeros del 1 al 5 
   for i in range(1,6): #itera del 1 al 5 (no incluye al 6)
    yield i #produce el valor de i y pausa la ejecucion 
    
# crear una instancia para el generador 
gen = contador() #gen es un objeto generador 

#interar sobre los valores producidos por el generador
for numero in gen:
    print(numero) #imprime cada numero producido por el generador.
