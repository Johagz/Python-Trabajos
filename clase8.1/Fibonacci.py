#Ejemplo fibonacci
def fibonacci():
    a,b=0,1 # inicializa los primeros dos numeros de la secuencia
    while True: #esto es un ciclo infinito para generar los numeros 
       yield a #produce el valor de a y pausa la ejecucion
       a,b=b, a +b # actualiza a y b para la siguiente iteracion
gen=fibonacci() #gen es un objeto generador que produce numeros de figonacci
#Obtener los primeros 10 numeros de fibonacci

for _ in range(10):
    print(next(gen)) #Obtiene el siguiente numero en la secuencia y lo imprime
