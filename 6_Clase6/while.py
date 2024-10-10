#Programa para adivinar un numero secreto
#Definimos el numero secreto

numero_secreto=7

#inicializar la variable para almacenar el numero del usuario

numero_adivinado=None

#Mensaje inicial
print("Adivina el numero secreto (entre 1 y 10):")

#Bucle while que continua hasta que el usuario adivine el numero secreto

while numero_adivinado!=numero_secreto:
    #solicitar al usuario que ingrese un numero
    numero_adivinado=int(input("introduce tu numero:"))
    #comprobar si el numero ingresado es correcto
    if numero_adivinado<numero_secreto:
        print("El numero ingresado es muy pequeño")
    elif numero_adivinado>numero_secreto:
        print("Demasiado alto intenta de nuevo")
    else:
        print("Adivinaste el numero Felicidades")
        
        
#Mensaje de cierre del juego
print("Gracias por Jugar")