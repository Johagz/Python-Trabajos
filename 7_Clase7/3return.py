#Ejemplo básico de return
def calcular_cuadrado(numero):
    return numero*numero
resultado= calcular_cuadrado(2)
print("Ejemplo de return:")
print(f"El cuadrado de 2 es: {resultado}")

#Ejemplo 2 de retoeno de multiples valores 
def Obtener_datos():
    nombre="Ana"
    Edad=23
    return nombre, Edad #retornara los valores como tuplas 
#Asignamos los valores a una variable
nombre, edad =Obtener_datos()
print("Ejemplo multiples Valores")
print(f"nombre: {nombre}, edad: {edad}")
print()


#Ejemplo 3 Retorno sin condicional 
def clasificar_numero(numero):
    if numero>0:
        return "positivo"
    elif numero<0:
        return "negativo"
    else:
        return "0"
    
resultado1=clasificar_numero(10)
resultado2=clasificar_numero(-5)
resultado3=clasificar_numero(0)
print("Ejemplo 3: Sin return")
print(f"El numero 10 es: {resultado1}")
print(f"El numero -5 es: {resultado2}")
print(f"El numero 0 es: {resultado3}")


#Ejemplo 4 Sin return
def mostrar_mensaje():
    print("Esta funcion no retorna valor")
    
resultado =mostrar_mensaje()
print("Ejemplo 4: Sin Retorno")
print(f"El valor retornado es: {resultado}")
