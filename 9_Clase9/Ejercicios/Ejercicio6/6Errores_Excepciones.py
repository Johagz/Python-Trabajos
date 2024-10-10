#Manejo de Errores y Excepciones 
try:
    num=float(input("Por Favor Ingrese un número:"))
    print(f"El número ingresado es:{num}")
except ValueError:
    print("No ingreso un número, por favor vuelva a intentar")
