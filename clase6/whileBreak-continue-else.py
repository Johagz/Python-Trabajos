#Programa que pide numeros hasta que se ingresa un numero negativo

#Inicializamos la variable suma para la suma de los numeros positivos 
suma=0

#inicializamos un ciclo usando while y true
while True:
    entrada=int(input("Introduzca un numero (negativo para terminar):"))
    
    #Verificar si el numero ingresado es negativo
    if entrada < 0:
        #si el numero es negativo salimos el ciclo
        print("se acaba el proceso")
        break
    #Sumamos el numero positivo ingresado a la variable suma 
    suma+=entrada
    #Verificar si el numero ingresado es par 
    if entrada %2==0:
        #si el numero es par usamos continue para saltar la impresion y pasar a la siguiente interacion del ciclo
        print("Continue")
        continue
    #Si el numero ingresado no es par (es impar) se ejecuta la linea
    print("NUMERO IMPAR INGRESADO:", entrada)
else:
    print("El ciclo ha terminado porque se ingreso un numero negativo")
    
print("la suma de los numeros ingresados es: ", suma)
