#Ejemplo 1: Funciones Anidadas
def funcion_externa(x):
    def funcion_interna(y):
        return y+10
    return funcion_interna(x) # llamada a la funcion interna con el valor de x

#llamada a la funcion extarna
resultado=funcion_externa(5)
print(f"Resultado de la funcion_Extaerna es: {resultado}")

#Ejemplo 2: closure o Cierre
def crear_multiplicador(factor):
    def multiplicador(x):
        return x * factor
    return multiplicador
duplicar=crear_multiplicador(2)
triplicar= crear_multiplicador(3)

print(f"Duplicar 10: {duplicar(10)}")
print(f"Triplicar 10: {triplicar(10)}")