#Ejercicio 8: Verificar el estado de un número con operador ternario

numero=int(input("Ingrese un número: "))

mensaje= f"El {numero} es un número positivo" if numero>0 else f"El {numero} es un número negativo" if numero<0 else "El numero es Cero" 

print(mensaje)